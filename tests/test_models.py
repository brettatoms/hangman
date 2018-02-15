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
        user = UserFactory(email='foo@bar.com', request_token='1234', access_token='578')
        user.save()

        retrieved = User.get_by_id(user.id)
        assert retrieved == user

    def test_created_at_defaults_to_datetime(self):
        """Test creation date."""
        user = UserFactory(email='foo@bar.com', request_token='1234', access_token='578')
        user.save()
        assert bool(user.created_at)
        assert isinstance(user.created_at, dt.datetime)

    def test_factory(self, db):
        """Test user factory."""
        user = UserFactory(email='foo@bar.com', request_token='1234', access_token='578')
        db.session.commit()
        assert bool(user.email)
        assert bool(user.created_at)
