from django.apps import AppConfig
from django.conf import settings
from django.db.models.signals import post_migrate
from django.contrib.auth.apps import AuthConfig


class BiodataConfig(AppConfig):
    name = 'biodata'

