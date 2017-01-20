# act_project/act/metadata/serializers.py
from rest_framework import serializers

from act.serializers import StdImageSerializer

from .models import (
    Metadata, OpenGraph, TwitterCard,
)


class OpenGraphSerializer(serializers.ModelSerializer):
    image = StdImageSerializer(read_only=True, variation='open_graph')

    class Meta:
        model = OpenGraph
        fields = ('type', 'url', 'title', 'description', 'image', )


class TwitterCardSerializer(serializers.ModelSerializer):
    image = StdImageSerializer(read_only=True, variation='twitter_card')

    class Meta:
        model = TwitterCard
        fields = ('card', 'title', 'description', 'image', )


class MetadataListSerializer(serializers.ModelSerializer):
    image = StdImageSerializer(read_only=True)

    class Meta:
        model = Metadata
        fields = (
            'url_name', 'title', 'description', 'robots', 'image', )


class MetadataDetailSerializer(serializers.ModelSerializer):
    open_graph = OpenGraphSerializer(read_only=True)
    twitter_card = TwitterCardSerializer(read_only=True)

    class Meta:
        model = Metadata
        fields = (
            'title', 'description', 'robots',
            'open_graph', 'twitter_card', )
