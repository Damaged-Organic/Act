# act_project/act/subscription/models.py
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.db import models

from .services import CheckoutHash


class SubscriberManager(models.Manager):
    def filter_active(self):
        return super(SubscriberManager, self).get_queryset().filter(
            is_active=True)


class Subscriber(models.Model):
    CheckoutHash = CheckoutHash()

    email = models.EmailField('E-mail', max_length=254)
    is_active = models.BooleanField('Активний', default=False)
    subscribed_at = models.DateTimeField(
        'Дата та час підписки', auto_now_add=True)
    checkout_at = models.DateTimeField(
        'Дата та час запиту', null=True, blank=True, default=None)
    checkout_hash = models.CharField(
        max_length=40, null=True, blank=True, default=None)

    objects = SubscriberManager()

    class Meta:
        verbose_name = 'Підписник'
        verbose_name_plural = 'Підписники'

    def __str__(self):
        return str(self.email) or self.__class__.__name__

    @property
    def is_unsubscribed(self):
        return (not self.is_active and not self.checkout_hash)

    def prepare_checkout_hash(self):
        self.checkout_hash = self.CheckoutHash.generate()
        self.checkout_at = timezone.now()

        return self.checkout_hash

    def validate_checkout(self, checkout_hash):
        if not self.checkout_hash:
            raise ValidationError(None)

        if not self.CheckoutHash.compare(self.checkout_hash, checkout_hash):
            raise ValidationError(None)

    def complete_checkout(self, checkout_hash):
        if self.is_active:
            self.unsubscribe()
        else:
            self.subscribe()

    def subscribe(self):
        self.checkout_hash = self.CheckoutHash.generate()
        self.checkout_at = None
        self.is_active = True

    def unsubscribe(self):
        self.checkout_hash = None
        self.checkout_at = timezone.now()
        self.is_active = False


class MailingManager(models.Manager):
    def latest_mailing(self):
        try:
            result = (
                super(MailingManager, self).get_queryset()
                .latest('mailing_at'))
        except self.model.DoesNotExist:
            result = None

        return result


class Mailing(models.Model):
    subscribers = models.ManyToManyField(
        Subscriber, blank=True, related_name='mailings')
    mailing_at = models.DateTimeField(
        'Дата та час розсилки', auto_now_add=True)

    objects = MailingManager()

    class Meta:
        verbose_name = 'Розсилка'
        verbose_name_plural = 'Розсилки'

    def __str__(self):
        return str(self.mailing_at) or self.__class__.__name__

    '''Subscribers shortcut methods'''

    def get_subscribers(self):
        return self.subscribers.all()

    def get_subscribers_count(self):
        return self.subscribers.count()
    get_subscribers_count.short_description = 'Кількість підписників'
