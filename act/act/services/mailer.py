# act_project/act/act/services/mailer.py
from collections import namedtuple

from django.core.exceptions import ImproperlyConfigured
from django.core.mail import get_connection, EmailMessage
from django.template.loader import render_to_string

from django.conf import settings


class MailerMixin():
    def __init__(self, *args, **kwargs):
        super(MailerMixin, self).__init__(*args, **kwargs)

        email_from_set = (
            hasattr(settings, 'EMAIL_FROM') and
            settings.EMAIL_FROM)

        email_to_set = (
            hasattr(settings, 'EMAIL_TO') and
            settings.EMAIL_TO)

        if not email_from_set or not email_to_set:
            raise ImproperlyConfigured('E-mail settings are not set.')

        self.email_from = settings.EMAIL_FROM
        self.email_to = settings.EMAIL_TO

        self.connection = get_connection()

    def send_email(
        self, subject, template, context, email_from=None, email_to=None
    ):
        email_html = render_to_string(template, context)

        if email_from is None:
            email_from = self.email_from
        email_from = "ДІЙ! <%s>" % email_from

        if email_to is None:
            email_to = self.email_to

        message = EmailMessage(
            subject, email_html, email_from, [email_to]
        )

        message.content_subtype = 'html'
        message.send()

    def send_mass_email(
        self, subject, template, context, email_from=None, recipient_list=None
    ):
        email_html = render_to_string(template, context)

        if email_from is None:
            email_from = self.email_from
        email_from = "ДІЙ! <%s>" % email_from

        if recipient_list is None:
            return

        messages = []
        for recepient in recipient_list:
            message = EmailMessage(
                subject, email_html, email_from, [recepient]
            )
            message.content_subtype = 'html'
            messages.append(message)

        if messages:
            self.connection.open()
            self.connection.send_messages(messages)
            self.connection.close()
            for m in messages: print(m.__dict__)
