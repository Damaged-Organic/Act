# act_project/act/website/serializers.py
import datetime

from django.conf import settings
from django.db.models import Prefetch
from django.db.models.fields.files import ImageFieldFile

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from act.services.mailer import MailerMixin

from .models import (
    IntroContent, AboutContent, GoalContent,
    Sponsor, Social, Activity,
    ProjectAttachedDocument, ProjectArea, Project,
    EventAttachedDocument, EventCategory, Event,
    City, Participant, Contact,
    Centre, CentreSubpage,
    Worksheet,
)
from .validators import (
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


class StdImageSerializer(serializers.ImageField):
    '''
    Output representation override to include thumbnail `variations`
    fields and present returned value as a complete dictionary
    '''
    def to_representation(self, value):
        representation = {
            'original': super().to_representation(value), }

        images = {
            key: image for key, image in value.__dict__.items()
            if isinstance(image, ImageFieldFile)}

        for field, image in images.items():
            representation.update({field: super().to_representation(image)})

        return representation


class AdjacentObjectsSerializerMixin(serializers.Serializer):
    '''
    This mixin adds to a serializer two fields that contain ids of previous
    and next records in database for a given serializer's model instance
    '''
    prev_id = serializers.SerializerMethodField()
    next_id = serializers.SerializerMethodField()

    def get_prev_id(self, instance):
        prev_instance = (
            instance._meta.model.objects.filter(id__lt=instance.id).last())
        return prev_instance.id if prev_instance else None

    def get_next_id(self, instance):
        next_instance = (
            instance._meta.model.objects.filter(id__gt=instance.id).first())
        return next_instance.id if next_instance else None


# Content

class IntroContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntroContent
        fields = ('id', 'name', 'headline', )


class AboutContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutContent
        fields = ('id', 'name', 'title', 'text', )


class GoalContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalContent
        fields = ('id', 'name', 'title', 'text', )


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
    photo = StdImageSerializer(read_only=True)

    class Meta:
        model = City
        fields = ('id', 'photo', 'name', )


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


# Participant

class ParticipantSerializer(ExcludableModelSerializer):
    photo = StdImageSerializer(read_only=True)
    centre = CentreCitySerializer(read_only=True)

    class Meta:
        model = Participant
        fields = ('id', 'photo', 'name', 'surname', 'position', 'centre', )

    @staticmethod
    def set_eager_loading(queryset):
        queryset = queryset.select_related('centre')

        return queryset


# Contact

class ContactSerializer(ExcludableModelSerializer):
    centre = CentreCitySerializer(read_only=True)

    class Meta:
        model = Contact
        fields = ('id', 'email', 'phone', 'address', 'centre', )

    @staticmethod
    def set_eager_loading(queryset):
        queryset = queryset.select_related('centre')

        return queryset


# Project (major and list)

class ProjectAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectArea
        fields = ('id', 'title', )


class ProjectAttachedDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectAttachedDocument
        fields = ('id', 'document', 'description', )


class ProjectListSerializer(ExcludableModelSerializer):
    image = StdImageSerializer(read_only=True)

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


# Event (major and list)

class EventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCategory
        fields = ('id', 'title', )


class EventAttachedDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventAttachedDocument
        fields = ('id', 'document', 'description', )


class EventListSerializer(ExcludableModelSerializer):
    image = StdImageSerializer(read_only=True)

    event_category = EventCategorySerializer(read_only=True)
    centres = CentreCitySerializer(read_only=True, many=True)
    project = ProjectListSerializer(read_only=True)

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


# Project (detail)

class ProjectDetailSerializer(
    AdjacentObjectsSerializerMixin, ExcludableModelSerializer
):
    image = StdImageSerializer(read_only=True)

    project_area = ProjectAreaSerializer(read_only=True)
    project_attached_documents = ProjectAttachedDocumentSerializer(
        read_only=True, many=True)
    centres = CentreCitySerializer(read_only=True, many=True)
    events = EventListSerializer(
        exclude_fields=['centres', 'project'], read_only=True, many=True)

    class Meta:
        model = Project
        fields = (
            'id', 'project_area', 'project_attached_documents',
            'centres', 'events',
            'started_at',  'image', 'title', 'content', 'is_active', 'slug',
            'prev_id', 'next_id',
        )

    @staticmethod
    def set_eager_loading(queryset):
        queryset = queryset.select_related('project_area')
        queryset = queryset.prefetch_related(
            'project_attached_documents',
            Prefetch(
                'events',
                queryset=Event.objects.select_related('event_category')),
            Prefetch(
                'centres',
                queryset=Centre.objects.select_related('city'))
        )

        return queryset


# Event (detail)

class EventDetailSerializer(
    AdjacentObjectsSerializerMixin, ExcludableModelSerializer
):
    image = StdImageSerializer(read_only=True)

    event_category = EventCategorySerializer(read_only=True)
    centres = CentreCitySerializer(read_only=True, many=True)
    project = ProjectListSerializer(read_only=True)
    event_attached_documents = EventAttachedDocumentSerializer(
        read_only=True, many=True)

    class Meta:
        model = Event
        fields = (
            'id', 'event_category', 'event_attached_documents',
            'centres', 'project',
            'created_at', 'image', 'title', 'content', 'is_active', 'slug',
            'prev_id', 'next_id',
        )

    @staticmethod
    def set_eager_loading(queryset):
        queryset = queryset.select_related('event_category', 'project')
        queryset = queryset.prefetch_related(
            'event_attached_documents',
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


# Centre

class CentreListSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    projects = ProjectListSerializer(
        exclude_fields=['centres'], read_only=True, many=True
    )
    events = EventListSerializer(
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
    contact = ContactSerializer(
        exclude_fields=['centre'], read_only=True
    )
    participants = ParticipantSerializer(
        exclude_fields=['centre'], read_only=True, many=True
    )
    projects = ProjectListSerializer(
        exclude_fields=['centres'], read_only=True, many=True
    )
    events = EventListSerializer(
        exclude_fields=['centres'], read_only=True, many=True
    )
    top_event = EventListSerializer(
        exclude_fields=['centres'], read_only=True
    )
    centres_subpages = CentreSubpageSerializer(
        exclude_fields=['centre'], read_only=True, many=True
    )

    class Meta:
        model = Centre
        fields = (
            'id', 'city', 'contact',
            'participants', 'projects', 'events', 'top_event',
            'centres_subpages',
            'short_description',
        )

    @staticmethod
    def set_eager_loading(queryset):
        queryset = queryset.select_related('city', 'contact', 'top_event')
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
