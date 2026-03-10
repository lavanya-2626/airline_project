"""
users/services.py — UserService: business logic for profile updates.
"""
import logging
from django.contrib.auth.models import User
from .models import UserProfile

logger = logging.getLogger('apps.users')


class UserService:

    @staticmethod
    def get_or_create_profile(user: User) -> UserProfile:
        """Return the profile for a user, creating one if missing."""
        profile, _ = UserProfile.objects.get_or_create(user=user)
        return profile

    @staticmethod
    def update_profile(user: User, data: dict) -> UserProfile:
        """
        Update both the User and UserProfile in one atomic operation.
        data dict keys: first_name, last_name, email, phone, nationality, city, country
        """
        # Update User fields
        user.first_name = data.get('first_name', user.first_name)
        user.last_name = data.get('last_name', user.last_name)
        user.email = data.get('email', user.email)
        user.save(update_fields=['first_name', 'last_name', 'email'])

        # Update Profile fields
        profile = UserService.get_or_create_profile(user)
        profile.phone = data.get('phone', profile.phone)
        profile.nationality = data.get('nationality', profile.nationality)
        profile.city = data.get('city', profile.city)
        profile.country = data.get('country', profile.country)
        profile.save()

        logger.info("Profile updated for user: %s", user.username)
        return profile
