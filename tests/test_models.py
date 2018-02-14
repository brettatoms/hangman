# -*- coding: utf-8 -*-
"""Model unit tests."""
import datetime as dt

import pytest

from hangman.user.models import User

from .factories import UserFactory


@pytest.mark.usefixtures('db')
class TestUser:
    """User tests."""

    def test_get_by_id(self):
        """Get user by ID."""
        user = User('foo@bar.com')
        user.save()

        retrieved = User.get_by_id(user.id)
        assert retrieved == user

    def test_created_at_defaults_to_datetime(self):
        """Test creation date."""
        user = User(email='foo@bar.com')
        user.save()
        assert bool(user.created_at)
        assert isinstance(user.created_at, dt.datetime)

    def test_factory(self, db):
        """Test user factory."""
        user = UserFactory(password='myprecious')
        db.session.commit()
        assert bool(user.email)
        assert bool(user.created_at)
        assert user.is_admin is False
        assert user.active is True
        assert user.check_password('myprecious')
