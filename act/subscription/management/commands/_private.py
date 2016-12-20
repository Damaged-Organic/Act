# act_project/act/subscription/management/commands/_private.py
from django.core.management.base import BaseCommand, CommandError

from ...models import Subscriber, Mailing


class Command(BaseCommand):
    help = 'Sends mail to all of the active subscribers in list'

    def get_subscribers(self):
        return Subscriber.objects.filter_active()

    def get_mailing(self):
        return Mailing.objects.latest_mailing()
