# act_project/act/website/management/commands/mailing.py
import datetime
import logging

from smtplib import SMTPException

from act.services.mailer import MailerMixin

from subscription.management.commands._private import Command as MailingCommand

from ...models import Event


class Command(MailerMixin, MailingCommand):
    def get_events(self, mailing=None):
        if mailing is None:
            events = Event.objects.order_by_created_at_limit()
        else:
            events = Event.objects.filter_created_at_gt(mailing.mailing_at)

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
            self.send_subscription_emails(subscribers, events)
        except Exception as e:
            file_logger = logging.getLogger('file')
            file_logger.error(repr(e))

        self.record_mailing(subscribers)

    def send_subscription_emails(self, subscribers, events):
        recepient_list = [subscriber.email for subscriber in subscribers]

        subject = 'Дайджест новин мережі ДІЙ!'
        template = 'website/emails/subscription.html'
        context = {
            'events': events,
            'sent_at': datetime.datetime.now(),
        }

        super(Command, self).send_mass_email(
            subject, template, context, None, recepient_list
        )
