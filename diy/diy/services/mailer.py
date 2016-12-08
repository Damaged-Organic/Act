# diy_project/diy/diy/services/mailer.py
from collections import namedtuple

from django.core.exceptions import ImproperlyConfigured
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from django.conf import settings


class MailerMixin():
    def __init__(self, *args, **kwargs):
        super(MailerMixin, self).__init__(*args, **kwargs)

        if ((not hasattr(settings, 'EMAIL_FROM') or
             not hasattr(settings, 'EMAIL_TO'))):
            raise ImproperlyConfigured('E-mail settings are not set')

        self.email_from = settings.EMAIL_FROM
        self.email_to = settings.EMAIL_TO

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
