from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users'
    label = 'users'

    def ready(self):
        # Connect signals so UserProfile is auto-created on user creation
        import apps.users.signals  # noqa: F401
