# act_project/act/act/settings/packages/logging.py
import os

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'simple': {
            'format': '[%(asctime)s] %(levelname)s %(message)s',
	    'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s',
	    'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'development_logfile': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.FileHandler',
            'filename': os.path.abspath(
                os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../')
            ) + '/django_dev.log',
            'formatter': 'verbose'
        },
        'production_logfile': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'filename': os.path.abspath(
                os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../')
            ) + '/django_production.log',
            'formatter': 'simple'
        },
        'dba_logfile': {
            'level': 'DEBUG',
            'filters': ['require_debug_false', 'require_debug_true'],
            'class': 'logging.FileHandler',
            'filename': os.path.abspath(
                os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../')
            ) + '/django_dba.log',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'coffeehouse': {
            'handlers': ['console', 'development_logfile', 'production_logfile'],
         },
        'dba': {
            'handlers': ['console', 'dba_logfile'],
        },
        'django': {
            'handlers': ['console', 'development_logfile', 'production_logfile'],
        },
        'py.warnings': {
            'handlers': ['console', 'development_logfile'],
        },
    }
}
