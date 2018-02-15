# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from random import choice

from flask import Blueprint, abort
from flask import current_app as app
from flask import jsonify, request
from flask_login import current_user, login_required
from sqlalchemy.sql.functions import sum

from hangman.database import db
from hangman.user.models import User

from .models import Game, GameStatus

blueprint = Blueprint('game', __name__, url_prefix='/games')

words_set = ['3dhubs', 'marvin', 'print', 'filament', 'order', 'layer']


@blueprint.route('', methods=['POST'])
@login_required
def create():
    """Create a game."""
    word = choice(words_set)
    game = Game(user=current_user, word=word)
    game.save()
    return jsonify(game.to_json())


@blueprint.route('/<int:game_id>')
@login_required
def get(game_id):
    """Get the game details."""
    game = Game.query.filter_by(id=game_id, user_id=current_user.id).first_or_404()
    return jsonify(game.to_json())


@blueprint.route('/<int:game_id>', methods=['PATCH'])
@login_required
def update(game_id):
    """Update a game."""
    game = Game.query.filter_by(id=game_id, user_id=current_user.id).first_or_404()
    if game.status != GameStatus.IN_PROGRESS.value:
        return abort(403)

    # TODO: validate guess
    guess = request.get_json()['guess']
    if guess not in game.guesses:
        guesses = list(game.guesses) # copy so the session will detect the change
        guesses.append(guess)
        game.guesses = guesses
        game.score = game.recalc_score()
        game.status = game.recalc_status()
        game.save()

    return jsonify(game.to_json())


@blueprint.route('/highscores')
@login_required
def highscores():
    """Update a game."""
    result = db.session.query(User.email, sum(Game.score).label('score'))\
                       .join(Game) \
                       .group_by(User.id) \
                       .order_by(db.desc('score')) \
                       .limit(10) \
                       .all()

    data = [{'email': row[0], 'score': row[1]} for row in result]
    return jsonify(data)
