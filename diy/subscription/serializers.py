# diy_project/diy/subscription/serializers.py
from rest_framework import serializers

from .models import Subscriber


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ('url_name', 'title', 'description', 'robots', )
