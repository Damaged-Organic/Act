# diy_project/diy/metadata/serializers.py
from rest_framework import serializers

from .models import Metadata


class MetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metadata
        fields = ('email', )
