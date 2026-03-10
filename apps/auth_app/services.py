"""
auth_app/services.py — AuthService: business logic for user registration
and authentication. Views delegate to this; no ORM calls live in views.
"""
import logging
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from apps.core.exceptions import UserAlreadyExistsError, AuthError

logger = logging.getLogger('apps.auth_app')


class AuthService:

    @staticmethod
    def register_user(username: str, email: str, password: str) -> User:
        """
        Create a new User. Raises UserAlreadyExistsError if the
        username or email is already taken.
        Returns the newly created User instance.
        """
        if User.objects.filter(username=username).exists():
            raise UserAlreadyExistsError('Username already taken.')
        if User.objects.filter(email=email).exists():
            raise UserAlreadyExistsError('Email already registered.')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )
        logger.info("New user registered: %s (%s)", username, email)
        return user

    @staticmethod
    def authenticate_user(request, username: str, password: str) -> User:
        """
        Authenticate credentials. Raises AuthError if invalid.
        Returns the authenticated User.
        """
        user = authenticate(request, username=username, password=password)
        if user is None:
            raise AuthError('Invalid username or password.')
        return user
