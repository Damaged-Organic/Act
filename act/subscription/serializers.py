# act_project/act/subscription/serializers.py
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

    def send_subscribe_email(self, subscriber):
        if not subscriber.id:
            raise Subscriber.DoesNotExist('Subscriber is not yet created')

        subscribe_subject = subscriber.subscribe_email.subject
        subscribe_body = subscriber.subscribe_email()

        super(SubscriberSerializer, self).send_email(
            subscribe_subject, subscribe_body, None, subscriber.email)

    def send_subscription_emails(self, subscribers, events):
        super(SubscriberSerializer, self).send_mass_email(
            subscribers,
            lambda subscriber: subscriber.subscription_email.subject,
            lambda subscriber: subscriber.subscription_email(events),
            lambda subscriber: subscriber.email,
            None)
