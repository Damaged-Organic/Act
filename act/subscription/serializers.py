# act_project/act/subscription/serializers.py
import datetime

from rest_framework.exceptions import ValidationError as RESTValidationError
from rest_framework import serializers

from act.services.mailer import MailerMixin

from .models import Subscriber


class SubscriberSerializer(MailerMixin, serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ('email', )

    def create(self, validated_data):
        subscriber, created = Subscriber.objects.update_or_create(
            **validated_data)

        if not subscriber.is_unsubscribed:
            raise RESTValidationError(None)

        return subscriber

    def send_subscribe_email(self, checkout_url):
        email_to = self.validated_data['email']

        subject = 'Підписка на новини мережі ДІЙ!'
        template = 'subscription/emails/subscribe.html'
        context = {
            'email': email_to,
            'checkout_url': checkout_url,
            'sent_at': datetime.datetime.now(),
        }

        super(SubscriberSerializer, self).send_email(
            subject, template, context, None, email_to
        )
