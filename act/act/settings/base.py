# act_project/act/act/settings/base.py
from os.path import join, abspath, dirname

# Base directory

BASE_DIR = join(abspath(dirname(__file__)), '../../')


# Root directory

def root(*dirs):
    return join(abspath(BASE_DIR), *dirs)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'django_cleanup',
    'django_filters',
    'django_bleach',
    'django_crontab',
    'rest_framework',
    'ckeditor',
    'stdimage',
    'metadata.apps.MetadataConfig',
    'subscription.apps.SubscriptionConfig',
    'website.apps.WebsiteConfig',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # CORS
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # HTML min
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
    # Website
    'website.middleware.security_headers_middleware.SecurityHeadersMiddleware',
]

ROOT_URLCONF = 'act.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # Project
            root('templates'),
            # Subscription application
            root('subscription', 'templates'),
            # Website application
            root('website', 'templates'),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ]),
            ],
        },
    },
]

WSGI_APPLICATION = 'act.wsgi.application'


# Databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':   'act',
        'OPTIONS': {
            'use_unicode': True,
            'charset': 'utf8',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}


# Password validation

PASSWORD_VALIDATION = 'django.contrib.auth.password_validation'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': PASSWORD_VALIDATION + '.UserAttributeSimilarityValidator',
    },
    {
        'NAME': PASSWORD_VALIDATION + '.MinimumLengthValidator',
    },
    {
        'NAME': PASSWORD_VALIDATION + '.CommonPasswordValidator',
    },
    {
        'NAME': PASSWORD_VALIDATION + '.NumericPasswordValidator',
    },
]


# Internationalization

LANGUAGE_CODE = 'uk'
LANGUAGES = (
    ('uk', 'UK'),
)

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True
USE_L10N = True
USE_TZ = True

LOCALE_PATHS = [
    root('website', 'locale'),
]


# Static files

STATIC_URL = '/static/'
STATIC_ROOT = root('static')

MEDIA_URL = '/uploads/'
MEDIA_ROOT = root('uploads')


# Admins

ADMINS = [
    ('Webmaster', 'webmaster@cheers-development.in.ua'),
]


# Packages

try:
    from .packages.transmeta import *
    from .packages.cors import *
    from .packages.bleach import *
    from .packages.ckeditor import *
    from .packages.crontab import *
    from .packages.metadata import *
    '''
    LOGGING is built using base directory path, so in order to
    access base settings variables logging settings are returned
    by function that takes all the neccesary arguments
    '''
    from .packages.logging import get_logging
    LOGGING = get_logging(BASE_DIR)
except ImportError:
    print('No packages settings are defined.')
