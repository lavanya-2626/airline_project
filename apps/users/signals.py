"""
users/signals.py — Automatically creates a UserProfile whenever a new
User is saved for the first time. Removes the lazy creation workaround
that was previously scattered in views.
"""
import logging
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import UserProfile

logger = logging.getLogger('apps.users')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        logger.info("UserProfile auto-created for user: %s", instance.username)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Keep profile in sync when user is updated."""
    if hasattr(instance, 'profile'):
        instance.profile.save()
