# diy_project/diy/website/serializers.py
from django.conf import settings
from rest_framework import serializers

from .models import (
    Sponsor, Social,
    ProjectArea, Project,
)


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
            'id', 'project_area', 'started_at', 'is_active', 'image', 'slug',
            'title', 'short_description', 'content',
        )
