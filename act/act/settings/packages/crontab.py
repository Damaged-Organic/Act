# act_project/act/act/settings/packages/crontab.py
CRONJOBS = [
    ('00 6 * * *', 'django.core.management.call_command', ['mailing']),
]
