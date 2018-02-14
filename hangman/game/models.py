# -*- coding: utf-8 -*-
"""User models."""
from enum import Enum

from hangman.database import Column, Model, SurrogatePK, db, reference_col, relationship


class GameStatus(Enum):
    """Represents a games state."""

    WON = 'won'
    IN_PROGRESS = 'in_progress'
    LOST = 'lost'


class Game(SurrogatePK, Model):
    """Game model."""

    __tablename__ = 'items'
    user_id = reference_col('users', nullable=False)
    user = relationship('User', backref='user_items')
    word = Column(db.String(32), nullable=False)
    guesses = Column(db.ARRAY(db.String(32)), default=[])

    MAX_GUESSES = 6

    @property
    def masked_word(self):
        if self.status == GameStatus.LOST:
            return self.word

        guesses = set(self.guesses)
        value = '*' * len(self.word)

        # replace the mask with the guessed characters
        for index, char in enumerate(self.word):
            if char in guesses:
                value = value[0:index] + char + value[index + 1:]

        return value

    @property
    def score(self):
        if self.status == GameStatus.LOST:
            return -1
        elif self.status == GameStatus.IN_PROGRESS:
            return 0
        return len(self.word) - len(self.guesses) + 1

    @property
    def status(self):
        if len(self.guesses) >= Game.MAX_GUESSES:
            return GameStatus.LOST

        word_set = set(self.word)
        guessed_correctly = self.word in self.guesses or set(self.guesses) & word_set == word_set
        return GameStatus.WON if guessed_correctly else GameStatus.IN_PROGRESS

    def __init__(self, **kwargs):
        """Create instance."""
        db.Model.__init__(self, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<Game({id})>'.format(id=self.id)

    def to_json(self):
        """Serialize the game model."""
        print(self.status)
        print(self.status.value)
        data = {
            'id': self.id,
            'status': self.status.value,
            'score': self.score,
            'guesses': self.guesses,
            'guesses_left': self.MAX_GUESSES - len(self.guesses),
            'word': self.masked_word
        }

        print(data)

        return data
