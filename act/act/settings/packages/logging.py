# act_project/act/act/settings/packages/logging.py
import os


def get_logging(base_dir):
    return {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'simple': {
                'format': '%(asctime)s %(levelname)s %(module)s %(message)s'
            },
            'verbose': {
                'format': (
                    '%(asctime)s %(levelname)s %(process)d %(thread)d '
                    '%(module)s %(message)s ')
            },
        },
        'filters': {
            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue',
            },
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse',
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'filters': ['require_debug_true'],
                'formatter': 'simple',
            },
            'file': {
                'level': 'ERROR',
                'class': 'logging.FileHandler',
                'filters': ['require_debug_false'],
                'formatter': 'verbose',
                'filename': os.path.join(base_dir, 'logs/django.log'),
            },
            'mail_admins': {
                'level': 'ERROR',
                'class': 'django.utils.log.AdminEmailHandler',
                'filters': ['require_debug_false'],
                'formatter': 'verbose',
            },
        },
        'loggers': {
            'django.security.DisallowedHost': {
                'handlers': ['file'],
                'level': 'ERROR',
                'propagate': False,
            },
            'commands': {
                'level': 'ERROR',
                'handlers': ['console', 'file', 'mail_admins'],
                'propagate': False,
            },
        },
    }
