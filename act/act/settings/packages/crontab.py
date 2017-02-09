# act_project/act/act/settings/packages/crontab.py
CRONJOBS = [
    ('0 6 * * *', 'django.core.management.call_command', ['mailing']),
]
