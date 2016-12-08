# diy_project/diy/subscription/serializers.py
import datetime

from rest_framework import serializers

from diy.services.mailer import MailerMixin

from .models import Subscriber


class SubscriberSerializer(MailerMixin, serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ('email', )

    def send_subscribe_email(self):
        # TODO: Here should be a checkout hash setup somehow. Or in the view.
        email_to = self.validated_data['email']

        subject = 'Підписка на новини мережі ДІЙ!'
        template = 'website/emails/subscribe.html'
        context = {
            'email': email_to,
            'sent_at': datetime.datetime.now(),
        }

        super(SubscriberSerializer, self).send_email(
            subject, template, context, None, email_to
        )

    def send_unsubscribe_email(self):
        return Email
