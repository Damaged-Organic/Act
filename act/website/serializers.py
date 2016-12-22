# act_project/act/website/serializers.py
import datetime

from django.conf import settings
from django.db.models import Prefetch

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from act.services.mailer import MailerMixin

from .models import (
    IntroContent,
    Sponsor, Social, Activity,
    ProjectArea, Project,
    EventCategory, Event,
    City, Participant, Contact,
    Centre, CentreSubpage,
    Worksheet,
    problem_description_validator,
    activity_description_validator,
)


class ExcludableModelSerializer(serializers.ModelSerializer):
    '''
    Allows to exclude fields to avoid duplicate nested model serialization
    '''
    def __init__(self, *args, **kwargs):
        exclude_fields = kwargs.pop('exclude_fields', None)
        super(ExcludableModelSerializer, self).__init__(*args, **kwargs)

        if exclude_fields:
            for field_name in exclude_fields:
                self.fields.pop(field_name)


# Content

class IntroContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntroContent
        fields = ('id', 'name', 'headline', )


# Links

class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('id', 'title', 'link', 'logo', )


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ('id', 'title', 'link', 'icon', )


# Activity

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('id', 'title', 'icon', )


# City

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'photo', 'photo_thumb', 'name', )


# Participant

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = (
            'id', 'photo', 'photo_thumb', 'name', 'surname', 'position',
        )


# Contant

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            'id', 'email', 'phone', 'address',
        )


# Centre (partial nested relation)

class CentreCitySerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)

    class Meta:
        model = Centre
        fields = ('id', 'city', )

    @staticmethod
    def set_eager_loading(queryset):
        queryset = queryset.select_related('city')

        return queryset


# Project

class ProjectAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectArea
        fields = ('id', 'title', )


class ProjectSerializer(ExcludableModelSerializer):
    project_area = ProjectAreaSerializer(read_only=True)
    centres = CentreCitySerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = (
            'id', 'project_area', 'centres',
            'started_at',  'image', 'title', 'content', 'is_active', 'slug',
        )

    @staticmethod
    def set_eager_loading(queryset):
        queryset = queryset.select_related('project_area')
        queryset = queryset.prefetch_related(
            Prefetch('centres', queryset=Centre.objects.select_related('city'))
        )

        return queryset


# Event

class EventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCategory
        fields = ('id', 'title', )


class EventSerializer(ExcludableModelSerializer):
    event_category = EventCategorySerializer(read_only=True)
    centres = CentreCitySerializer(read_only=True, many=True)
    project = ProjectSerializer(read_only=True)

    class Meta:
        model = Event
        fields = (
            'id', 'event_category', 'centres', 'project',
            'created_at', 'image', 'title', 'content', 'is_active', 'slug',
        )

    @staticmethod
    def set_eager_loading(queryset):
        queryset = queryset.select_related('event_category', 'project')
        queryset = queryset.prefetch_related(
            Prefetch('centres', queryset=Centre.objects.select_related('city'))
        )

        return queryset


# CentreSubpage

class CentreSubpageSerializer(ExcludableModelSerializer):
    centre = CentreCitySerializer(read_only=True)

    class Meta:
        model = CentreSubpage
        fields = (
            'id', 'centre', 'headline', 'content',
        )

    @staticmethod
    def set_eager_loading(queryset):
        queryset = queryset.select_related('centre', 'centre__city')

        return queryset


# Centre (partial nested relations)

class CentreProjectsSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    projects = ProjectSerializer(
        exclude_fields=['centres'], read_only=True, many=True
    )

    class Meta:
        model = Centre
        fields = ('id', 'city', 'projects', )

    @staticmethod
    def set_eager_loading(queryset):
        queryset = queryset.select_related('city')
        queryset = queryset.prefetch_related(
            Prefetch(
                'projects',
                queryset=Project.objects.select_related('project_area'))
        )

        return queryset


class CentreEventsSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    events = EventSerializer(
        exclude_fields=['centres'], read_only=True, many=True
    )

    class Meta:
        model = Centre
        fields = ('id', 'city', 'events', )

    @staticmethod
    def set_eager_loading(queryset):
        queryset = queryset.select_related('city')
        queryset = queryset.prefetch_related(
            Prefetch(
                'events',
                queryset=Event.objects.select_related('event_category'))
        )

        return queryset


# Centre

class CentreListSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    projects = ProjectSerializer(
        exclude_fields=['centres'], read_only=True, many=True
    )
    events = EventSerializer(
        exclude_fields=['centres'], read_only=True, many=True
    )

    class Meta:
        model = Centre
        fields = (
            'id', 'city', 'projects', 'events',
        )

    @staticmethod
    def set_eager_loading(queryset):
        queryset = queryset.select_related('city')
        queryset = queryset.prefetch_related(
            Prefetch(
                'projects',
                queryset=Project.objects.select_related('project_area')),
            Prefetch(
                'events',
                queryset=Event.objects.select_related('event_category'))
        )

        return queryset


class CentreDetailSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    contact = ContactSerializer(read_only=True)
    participants = ParticipantSerializer(read_only=True, many=True)
    projects = ProjectSerializer(read_only=True, many=True)
    events = EventSerializer(read_only=True, many=True)
    centres_subpages = CentreSubpageSerializer(
        exclude_fields=['centre'], read_only=True, many=True
    )

    class Meta:
        model = Centre
        fields = (
            'id', 'city', 'contact',
            'participants', 'projects', 'events', 'centres_subpages',
            'short_description',
        )

    @staticmethod
    def set_eager_loading(queryset):
        queryset = queryset.select_related('city', 'contact')
        queryset = queryset.prefetch_related(
            Prefetch('participants', queryset=Participant.objects.all()),
            Prefetch(
                'projects',
                queryset=Project.objects.select_related('project_area')),
            Prefetch(
                'events',
                queryset=Event.objects.select_related('event_category'))
        )

        return queryset


# Worksheet

class WorksheetSerializer(MailerMixin, serializers.ModelSerializer):
    class Meta:
        model = Worksheet
        fields = (
            'full_name', 'residence', 'email', 'phone', 'personal_link',
            'problem', 'problem_description',
            'activity', 'activity_description',
        )

    def validate_problem_description(self, value):
        '''
        Defining validators on field level to stack them with default ones
        '''

        problem = 'problem' in self.initial_data and bool(
            self.initial_data['problem']) or False

        error_problem_description = problem_description_validator(
            problem, value)
        if error_problem_description:
            raise ValidationError(error_problem_description)

        return value

    def validate_activity_description(self, value):
        '''
        Defining validators on field level to stack them with default ones
        '''

        activity = 'activity' in self.initial_data and bool(
            self.initial_data['activity']) or False

        error_activity_description = activity_description_validator(
            activity, value)
        if error_activity_description:
            raise ValidationError(error_activity_description)

        return value

    def send_email(self):
        sent_at = datetime.datetime.now()

        subject = (
            'Нова анкета з сайту ДІЙ!, ' +
            sent_at.strftime('%d-%m-%Y %H:%M')
        )
        template = 'website/emails/worksheet.html'
        context = {
            'full_name': self.validated_data['full_name'],
            'residence': self.validated_data['residence'],
            'email': self.validated_data['email'],
            'phone': self.validated_data['phone'],
            'personal_link': self.validated_data['personal_link'],
            'problem_description':
                self.validated_data['problem_description'],
            'activity_description':
                self.validated_data['activity_description'],
            'sent_at': sent_at,
        }

        super(WorksheetSerializer, self).send_email(subject, template, context)
