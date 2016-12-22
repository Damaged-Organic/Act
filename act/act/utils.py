# act_project/act/act/utils.py
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings


def get_default_URL():
    default_url = (
        hasattr(settings, 'DEFAULT_URL') and
        settings.DEFAULT_URL)

    if not default_url:
        raise ImproperlyConfigured('Default URL setting is not set.')

    return default_url
