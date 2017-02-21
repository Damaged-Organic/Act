# act_project/act/subscription/views_api.py
from django.core.exceptions import ValidationError
from django.db import transaction

from rest_framework.exceptions import (
    ParseError, ValidationError as RESTValidationError
)
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    RetrieveModelMixin, CreateModelMixin, UpdateModelMixin
)

from .models import Subscriber
from .serializers import SubscriberSerializer


class SubscriberList(CreateModelMixin, GenericAPIView):
    serializer_class = SubscriberSerializer
    queryset = Subscriber.objects.all()

    def perform_create(self, serializer):
        '''
        Send a subscription confirmation e-mail on succesfull serializer save
        '''
        with transaction.atomic():
            subscriber = serializer.save()

            subscriber.prepare_checkout_hash()
            subscriber.save()

            serializer.send_subscribe_email(subscriber)

    def post(self, request, *args, **kwargs):
        try:
            return self.create(request, *args, **kwargs)
        except RESTValidationError:
            raise ParseError('Недійсні дані підписника.')


class SubscriberDetail(RetrieveModelMixin, UpdateModelMixin, GenericAPIView):
    serializer_class = SubscriberSerializer
    queryset = Subscriber.objects.all()

    def get_object(self):
        instance = super(SubscriberDetail, self).get_object()
        instance.validate_checkout(self.kwargs['checkout_hash'])

        return instance

    def perform_update(self, serializer):
        with transaction.atomic():
            subscriber = serializer.save()
            subscriber.complete_checkout(self.kwargs['checkout_hash'])
            subscriber.save()

    def get(self, request, *args, **kwargs):
        try:
            return self.retrieve(request, *args, **kwargs)
        except ValidationError:
            raise ParseError('Недійсні дані підписника.')

    def patch(self, request, *args, **kwargs):
        try:
            return self.partial_update(request, *args, **kwargs)
        except ValidationError:
            raise ParseError('Недійсні дані для оновлення статусу підписки.')
