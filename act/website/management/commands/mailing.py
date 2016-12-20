# act_project/act/website/management/commands/mailing.py
from subscription.management.commands._private import Command as MailingCommand

from ...models import Event
from ...serializers import EventSerializer


class Command(MailingCommand):
    def handle(self, *args, **options):
        subscribers = self.get_subscribers()

        if not subscribers.exists():
            return

        mailing = self.get_mailing()

        if mailing is None:
            events = Event.objects.order_by_created_at_limit()
        else:
            events = Event.objects.filter_created_at_gt(mailing.mailing_at)

        if not events.exists():
            return

        # Write custom serializer for this Email
        for event in EventSerializer(events, many=True).data:
            print(event)
