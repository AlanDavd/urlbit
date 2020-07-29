"""Shotener app."""

# Django
from django.apps import AppConfig


class ShortenerConfig(AppConfig):
    """Shortener app config"""

    name = 'urlbit.shortener'
    verbose_name = 'Shortener'
