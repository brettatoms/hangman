# -*- coding: utf-8 -*-
"""User models."""
import datetime as dt

from flask_login import UserMixin

from hangman.database import Column, Model, SurrogatePK, db


class User(UserMixin, SurrogatePK, Model):
    """A user of the app."""

    __tablename__ = 'users'
    email = Column(db.String(80), unique=True, nullable=False)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)

    access_token = Column(db.String(128), nullable=False)
    request_token = Column(db.String(128), nullable=False)

    def __init__(self, email, **kwargs):
        """Create instance."""
        db.Model.__init__(self, email=email, **kwargs)

    @property
    def full_name(self):
        """Full user name."""
        return '{0} {1}'.format(self.first_name, self.last_name)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<User({username!r})>'.format(username=self.username)
