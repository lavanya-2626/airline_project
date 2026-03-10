from django.apps import AppConfig


class FlightsConfig(AppConfig):
    default_auto_field = 'django_mongodb_backend.fields.ObjectIdAutoField'
    name = 'apps.flights'
    label = 'flights'
