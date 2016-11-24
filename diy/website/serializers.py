# diy_project/diy/website/serializers.py
from django.conf import settings
from rest_framework import serializers

from .models import (
    IntroContent,
    Sponsor, Social,
    ProjectArea, Project,
    EventCategory, Event,
)


class IntroContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntroContent
        fields = ('id', 'name', 'headline', )


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('id', 'title', 'link', 'logo', )


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ('id', 'title', 'link', 'icon', )


class ProjectAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectArea
        fields = ('id', 'title', )


class ProjectSerializer(serializers.ModelSerializer):
    project_area = ProjectAreaSerializer(read_only=True)

    class Meta:
        model = Project
        fields = (
            'id', 'project_area', 'started_at',  'image', 'title',
            'short_description', 'content', 'is_active', 'slug',
        )


class EventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCategory
        fields = ('id', 'title', )


class EventSerializer(serializers.ModelSerializer):
    event_category = EventCategorySerializer(read_only=True)
    project = ProjectSerializer(read_only=True)

    class Meta:
        model = Event
        fields = (
            'id', 'event_category', 'project', 'created_at', 'image',
            'title', 'short_description', 'content', 'is_active', 'slug',
        )
