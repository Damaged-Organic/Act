# act_project/act/act/settings/packages/ckeditor.py
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
