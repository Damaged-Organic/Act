# diy_project/diy/subscription/models.py
from django.core.exceptions import ValidationError
from django.db import models

from .services import CheckoutHash


class Subscriber(models.Model):
    email = models.EmailField('E-mail', max_length=254)
    is_active = models.BooleanField('Активний', default=False)
    subscribed_at = models.DateTimeField(
        'Дата та час підписки', auto_now_add=True)

    checkout_hash_in = models.CharField(
        max_length=40, null=True, blank=True, default=None)
    checkout_hash_out = models.CharField(
        max_length=40, null=True, blank=True, default=None)

    class Meta:
        verbose_name = 'Підписник'
        verbose_name_plural = 'Підписники'

    def __str__(self):
        return str(self.email) or self.__class__.__name__

    def subscribe(self, checkout_hash_in):
        if CheckoutHash.compare(self.checkout_hash_in, checkout_hash_in):
            raise ValidationError('Untrusted subscription attempt.')

        self.is_active = True
        self.checkout_hash_in = None

    def unsubscribe(self, checkout_hash_out):
        if CheckoutHash.compare(self.checkout_hash_out, checkout_hash_out):
            raise ValidationError('Untrusted unsubscription attempt.')

        self.is_active = False
        self.checkout_hash_out = None
