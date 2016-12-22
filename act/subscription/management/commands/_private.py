# act_project/act/subscription/management/commands/_private.py
import datetime

from django.core.management.base import BaseCommand, CommandError

from ...models import Subscriber, Mailing


class Command(BaseCommand):
    help = 'Should send mail to all of the active subscribers in list'

    def get_subscribers(self):
        return Subscriber.objects.filter_active()

    def get_mailing(self):
        return Mailing.objects.latest_mailing()

    def record_mailing(self, subscribers):
        mailing = Mailing(mailing_at=datetime.datetime.now())
        mailing.save()

        mailing.subscribers.set(subscribers)
        mailing.save()
