# diy_project/diy/subscription/views_api.py
from django.http import Http404

from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin

from .models import Subscriber
from .serializers import SubscriberSerializer


class SubscriberList(CreateModelMixin, GenericAPIView):
    serializer_class = SubscriberSerializer
    queryset = Subscriber.objects.all()

    def perform_create(self, serializer):
        '''
        Send a subscription confirmation e-mail on succesfull serializer save
        '''
        serializer.save()
        serializer.send_subscribe_email()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SubscriberDetail(UpdateModelMixin, GenericAPIView):
    serializer_class = SubscriberSerializer
    queryset = Subscriber.objects.all()

    # def perform_create(self, serializer):
    #     queryset = SignupRequest.objects.filter(user=self.request.user)
    #     if queryset.exists():
    #         raise ValidationError('You have already signed up')
    #     serializer.save(user=self.request.user)
    #
    # def perform_update(self, serializer):
    #     instance = serializer.save()
    #     send_email_confirmation(user=self.request.user, modified=instance)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
