# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import Blueprint, abort
from flask import current_app as app
from flask import jsonify, request
from flask_login import login_required

from .models import Game, GameStatus

blueprint = Blueprint('game', __name__, url_prefix='/games')


@blueprint.route('', methods=['POST'])
@login_required
def create():
    """Create a game."""
    game = Game(user=request.user)
    game.save()
    return jsonify(game.to_json())


@blueprint.route('/<int:game_id>')
@login_required
def get(game_id):
    """Get the game details."""
    game = Game.query.filter_by(id=game_id, user_id=request.user.id).first_or_404()
    return jsonify(game.to_json())


@blueprint.route('/<int:id>', methods=['PATCH'])
@login_required
def update(game_id):
    """Update a game."""
    game = Game.query.filter_by(id=game_id, user_id=request.user.id).first_or_404()
    if game.status != GameStatus.IN_PROGRESS:
        return abort(403)

    guess = request.args['guess']
    # TODO: validate guess
    game.guesses.append(guess)
    game.save()
    return jsonify(game.to_json())
