# diy_project/diy/diy/settings/base.py
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../')
)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'nested_admin',
    'django_bleach',
    'ckeditor',
    'metadata.apps.MetadataConfig',
    'website.apps.WebsiteConfig',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
    'website.middleware.security_headers_middleware.SecurityHeadersMiddleware',
]

ROOT_URLCONF = 'diy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'website/templates'),
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

WSGI_APPLICATION = 'diy.wsgi.application'

# Databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':   'diy',
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

TRANSMETA_DEFAULT_LANGUAGE = 'uk'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'website/locale'),
]

MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

# Security

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

# Bleach

BLEACH_ALLOWED_TAGS = ['span']
BLEACH_STRIP_TAGS = True

# CKEditor

CKEDITOR_CONFIGS = {
    'article_toolbar': {
        'toolbar_Article': [
            {'name': 'basic', 'items': [
                'Source', 'Maximize', 'RemoveFormat',
            ]},
            {'name': 'font_style', 'items': [
                'Bold', 'Italic', 'Underline', 'Strike',
                'Subscript', 'Superscript',
            ]},
            {'name': 'list', 'items': [
                'NumberedList', 'BulletedList',
            ]},
            {'name': 'justify', 'items': [
                'JustifyLeft', 'JustifyCenter', 'JustifyRight',
            ]},
            {'name': 'link', 'items': [
                'Link', 'Unlink', 'Anchor',
            ]},
            {'name': 'insert', 'items': [
                'Image',
            ]},
        ],
        'toolbar': 'Article',
        'tabSpaces': 4,
    },
}

# Socials

SOCIALS = {
    'facebook': '',
    'vkontakte': '',
    'twitter': '',
    'youtube': '',
}
