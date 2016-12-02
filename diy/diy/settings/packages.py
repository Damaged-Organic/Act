# diy_project/diy/diy/settings/packages.py

# Transmeta

TRANSMETA_DEFAULT_LANGUAGE = 'uk'
TRANSMETA_LANGUAGES = (
    ('uk', 'UK'),
)

# CORS

CORS_ORIGIN_WHITELIST = (
    'act.org.ua',
    'localhost:3333',
    '127.0.0.1:3333',
    'localhost:8000',
    '127.0.0.1:8000',
)

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
