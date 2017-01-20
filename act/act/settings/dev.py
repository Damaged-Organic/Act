# act_project/act/act/settings/dev.py
from .base import *

DEBUG = True


# Hosts

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', ]
INTERNAL_IPS = ('127.0.0.1', )

DEFAULT_URL = 'http://{}:8000'.format(ALLOWED_HOSTS[0])


# Application definition

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE_CLASSES += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


# Minify

HTML_MINIFY = False


# Database

DATABASES['default'].update({
    'HOST':     'localhost',
    'PORT':     '3306',
    'USER':     'root',
    'PASSWORD': 'root',
})


# Email

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

SERVER_EMAIL = EMAIL_HOST_USER

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
DEFAULT_TO_EMAIL = ''


# Secret key

SECRET_KEY = 'Something secret steers at us!'
