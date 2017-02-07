# act_project/act/website/serializers.py
import datetime

from django.db.models import Prefetch

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from act.serializers import StdImageSerializer
from act.services.mailer import MailerMixin

from .models import (
    IntroContent, AboutContent, GoalContent, DisclaimerContent,
    Sponsor, Social, Activity, Partner,
    ProjectAttachedDocument, ProjectArea, Project,
    EventAttachedDocument, EventCategory, Event,
    City, Participant, Contact,
    Centre, CentreSubpage,
    Worksheet,
    Scraping,
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


class AdjacentObjectsSerializerMixin(serializers.Serializer):
    '''
    This mixin adds to a serializer two fields that contain ids of previous
    and next records in database for a given serializer's model instance.
    It works ONLY when given model's Meta class `ordering` attribute is
    specified and ONLY if there's one or two ordering fields (with second
    beeing a primary key). No purpose for making it dynamic for now
    '''
    prev_object = serializers.SerializerMethodField()
    next_object = serializers.SerializerMethodField()

    def get_adjacent_instance(self, instance, method):
        Meta, Model = instance._meta, instance._meta.model
        adjacent_instance = None

        if hasattr(Meta, 'ordering') and Meta.ordering:
            ordering_field = Meta.ordering[0].replace('-', '')

            get_by = getattr(Model, '%s_by_%s' % (method, ordering_field))

            try:
                adjacent_instance = get_by(instance)
            except Model.DoesNotExist:
                pass

        return adjacent_instance

    def get_prev_object(self, instance):
        prev_instance = self.get_adjacent_instance(instance, 'get_previous')

        return self.serialize_adjacent_object(prev_instance)

    def get_next_object(self, instance):
        next_instance = self.get_adjacent_instance(instance, 'get_next')

        return self.serialize_adjacent_object(next_instance)

    def serialize_adjacent_object(self, instance):
        if instance and hasattr(instance, 'slug'):
            adjacent_object = {'id': instance.id, 'slug': instance.slug}
        else:
            adjacent_object = None

        return adjacent_object


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


class DisclaimerContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisclaimerContent
        fields = ('id', 'title', 'text_uk', 'text_en', )


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


# Partner

class PartnerSerializer(serializers.ModelSerializer):
    logo = StdImageSerializer(read_only=True)

    class Meta:
        model = Partner
        fields = ('id', 'logo', 'name', 'link', )


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
        fields = ('id', 'email', 'phone', 'address', 'centre', 'social_link', )

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
            'started_at', 'modified_at', 'image', 'title', 'content',
            'is_active', 'slug',
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
            'started_at', 'modified_at', 'image', 'title', 'content',
            'is_active', 'slug',
            'prev_object', 'next_object',
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
            'prev_object', 'next_object',
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
            'id', 'centre', 'headline', 'content', 'slug',
        )

    @staticmethod
    def set_eager_loading(queryset):
        queryset = queryset.select_related('centre__city')

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


# Scraping

class ScrapingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scraping
        fields = ('path', 'head', )

    def create(self, validated_data):
        scraping, created = Scraping.objects.update_or_create(
            path=validated_data.get('path', None),
            defaults={
                'path': validated_data.get('path', None),
                'head': validated_data.get('head', None)}, )

        return scraping
