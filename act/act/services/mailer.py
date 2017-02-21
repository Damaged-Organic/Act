# act_project/act/act/services/mailer.py
from django.core.exceptions import ImproperlyConfigured
from django.core.mail import get_connection, EmailMessage

from django.conf import settings


class MailerMixin():
    def __init__(self, *args, **kwargs):
        super(MailerMixin, self).__init__(*args, **kwargs)

        email_from_set = (
            hasattr(settings, 'DEFAULT_FROM_EMAIL') and
            settings.DEFAULT_FROM_EMAIL)

        email_to_set = (
            hasattr(settings, 'DEFAULT_TO_EMAIL') and
            settings.DEFAULT_TO_EMAIL)

        if not email_from_set or not email_to_set:
            raise ImproperlyConfigured('E-mail settings are not set.')

        self.email_from = settings.DEFAULT_FROM_EMAIL
        self.email_to = settings.DEFAULT_TO_EMAIL

        self.connection = get_connection()

    def get_email_from(self, email_from):
        if email_from is None:
            email_from = self.email_from
        return "ДІЙ! <%s>" % email_from

    def send_email(self, subject, body, email_from=None, email_to=None):
        email_from = self.get_email_from(email_from)

        if email_to is None:
            email_to = self.email_to

        if body is None:
            return

        message = EmailMessage(
            subject, body, email_from, [email_to])
        message.content_subtype = 'html'
        message.send()

    def send_mass_email(
            self, recipients, subject_lambda, body_lambda, email_to_lambda,
            email_from=None):
        '''
        As it's required to send custom email body that includes data
        related to recipient itself and incapsulated within calling method,
        we can utilize callables that return data based on given recipient.

        `*_lambda` arguments here are actually a callables which return custom
        recipient's email_to, subject and body without tight coupling to
        recipient object instance itself.
        '''
        email_from = self.get_email_from(email_from)

        if recipients is None:
            return

        messages = []
        for recipient in recipients:
            subject = subject_lambda(recipient)
            body = body_lambda(recipient)
            email_to = email_to_lambda(recipient)

            message = EmailMessage(
                subject, body, email_from, [email_to])
            message.content_subtype = 'html'

            messages.append(message)

        if messages:
            self.connection.open()
            self.connection.send_messages(messages)
            self.connection.close()
