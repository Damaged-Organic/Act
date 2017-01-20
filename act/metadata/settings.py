# act_project/act/metadata/settings.py
from django.conf import settings as django_settings


class Settings(object):
    DEFAULTS = {
        'SUPPORTED_MODELS': {},
    }

    @property
    def SUPPORTED_MODELS(self):
        return getattr(
            django_settings,
            'SUPPORTED_MODELS',
            self.DEFAULTS['SUPPORTED_MODELS'])


settings = Settings()
