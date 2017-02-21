# act_project/act/website/management/commands/mailing.py
import logging

from act.services.mailer import MailerMixin

from website.models import Event

from ._private import Command as MailingCommand

from ...serializers import SubscriberSerializer


class Command(MailerMixin, MailingCommand):
    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

        self.serializer = SubscriberSerializer()
        self.logger = logging.getLogger('commands')

    def get_events(self, mailing=None):
        if mailing is None:
            events = Event.objects.filter_active_limit()
        else:
            events = Event.objects.filter_active_created_at_gt(
                mailing.mailing_at)

        return events

    def handle(self, *args, **options):
        subscribers = self.get_subscribers()
        if not subscribers.exists():
            return

        mailing = self.get_mailing()

        events = self.get_events(mailing)
        if not events.exists():
            return

        try:
            self.serializer.send_subscription_emails(subscribers, events)
        except Exception as e:
            self.logger.error(repr(e))
            return

        self.record_mailing(subscribers)
