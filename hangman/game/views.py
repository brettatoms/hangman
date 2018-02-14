# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from random import sample

from flask import Blueprint, abort
from flask import current_app as app
from flask import jsonify, request
from flask_login import current_user, login_required

from .models import Game, GameStatus

blueprint = Blueprint('game', __name__, url_prefix='/games')

words_set = {'3dhubs', 'marvin', 'print', 'filament', 'order', 'layer'}


@blueprint.route('', methods=['POST'])
@login_required
def create():
    """Create a game."""
    word = sample(words_set, 1)[0]
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
    if game.status != GameStatus.IN_PROGRESS:
        return abort(403)

    # TODO: validate guess
    guess = request.get_json()['guess']
    guesses = set(game.guesses)  # make sure list is unique
    guesses.add(guess)
    game.guesses = list(guesses)
    game.save()

    print('returning')
    return jsonify(game.to_json())
