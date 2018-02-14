# -*- coding: utf-8 -*-
"""User models."""
from enum import Enum

from hangman.database import Column, Model, SurrogatePK, db, reference_col, relationship


class GameStatus(Enum):
    WON = 'won',
    IN_PROGRESS = 'in_progress',
    LOST = 'lost'


class Game(SurrogatePK, Model):
    __tablename__ = 'items'
    user_id = reference_col('users', nullable=False)
    user = relationship('User', backref='user_items')
    word = Column(db.String(32), nullable=False)
    guesses = Column(db.ARRAY(db.CHAR))

    MAX_GUESSES = 6

    @property
    def score(self):
        if self.status == GameStatus.LOST:
            return -1
        elif self.status == GameStatus.IN_PROGRESS:
            return 0
        return len(self.word) - len(self.guesses) + 1

    @property
    def status(self):
        if len(self.guesses) > Game.MAX_GUESSES:
            return GameStatus.LOST

        word_set = set(self.word)
        guessed_correctly = set(self.guesses) & word_set == word_set
        return GameStatus.WON if guessed_correctly else GameStatus.IN_PROGRESS

    def __init__(self, **kwargs):
        """Create instance."""
        db.Model.__init__(self, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<Item({id})>'.format(id=self.data['item_id'])

    def to_json(self):
        data = {
            'id': self.id,
            'status': self.status,
            'score': self.score,
            'guesses': self.guesses
        }

        if self.status != GameStatus.IN_PROGRESS:
            data['word'] == self.word

        return data
