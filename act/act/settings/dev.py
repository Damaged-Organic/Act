# act_project/act/act/settings/dev.py
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', ]
INTERNAL_IPS = ('127.0.0.1', )

SECRET_KEY = 'Something secret steers at us!'

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

EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

EMAIL_FROM = ''
EMAIL_TO = ''
