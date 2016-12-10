# diy_project/diy/subscription/views_api.py
from django.core.exceptions import ValidationError

from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from rest_framework.reverse import reverse

from .models import Subscriber
from .serializers import SubscriberSerializer


class SubscriberList(CreateModelMixin, GenericAPIView):
    serializer_class = SubscriberSerializer
    queryset = Subscriber.objects.all()

    def perform_create(self, serializer):
        '''
        Send a subscription confirmation e-mail on succesfull serializer save
        '''
        subscriber = serializer.save()

        checkout_hash = subscriber.checkout()
        checkout_url = reverse(
            'subscribers_detail_subscribe',
            args=[subscriber.pk, checkout_hash],
            request=self.request)
        serializer.send_subscribe_email(checkout_url)

        subscriber.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SubscriberDetail(UpdateModelMixin, GenericAPIView):
    serializer_class = SubscriberSerializer
    queryset = Subscriber.objects.all()

    def perform_update(self, serializer):
        subscriber = serializer.save()

        try:
            if not subscriber.is_active:
                subscriber.subscribe(self.kwargs['checkout_hash'])
            else:
                subscriber.unsubscribe(self.kwargs['checkout_hash'])
        except ValidationError as e:
            raise ParseError(e.message)

        subscriber.save()

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
