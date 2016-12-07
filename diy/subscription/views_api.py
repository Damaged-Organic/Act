# diy_project/diy/subscription/views_api.py
from rest_framework.generics import CreateAPIView

from .models import Subscriber
from .serializers import SubscriberSerializer


class SubscriberCreate(CreateAPIView):
    serializer_class = SubscriberSerializer
    queryset = Subscriber.objects.all()
