# act_project/act/website/views_api.py
from django.http import Http404

from rest_framework.response import Response
from rest_framework.generics import (
    GenericAPIView, ListAPIView, RetrieveAPIView, CreateAPIView,
)
from rest_framework.mixins import (
    CreateModelMixin, UpdateModelMixin,
)
from rest_framework.pagination import (
    LimitOffsetPagination, PageNumberPagination,
)

from django_filters import rest_framework as django_filters

from act.serializers import set_eager_loading

from .models import (
    IntroContent, AboutContent, GoalContent,
    Sponsor, Social, Activity,
    ProjectArea, Project,
    EventCategory, Event,
    City, Participant, Contact,
    Centre, CentreSubpage,
    Worksheet,
)
from .serializers import (
    IntroContentSerializer, AboutContentSerializer, GoalContentSerializer,
    SponsorSerializer, SocialSerializer, ActivitySerializer,
    ProjectAreaSerializer, ProjectListSerializer, ProjectDetailSerializer,
    EventCategorySerializer, EventListSerializer, EventDetailSerializer,
    CitySerializer, ParticipantSerializer, ContactSerializer,
    CentreListSerializer, CentreDetailSerializer, CentreCitySerializer,
    CentreSubpageSerializer,
    WorksheetSerializer,
)


# Content

class SingularItemAPIView(GenericAPIView):
    '''
    This view is tricky, as it overrides common behavior of `get_object()`
    method. It does not require positional `pk` argument, because it's
    intention is to return first & only one object of a given queryset
    '''
    def get_object(self):
        instance = self.get_queryset().first()
        return instance

    def get(self, request, format=None):
        singular_content = self.get_object()

        if not singular_content:
            raise Http404

        serializer_class = self.get_serializer_class()
        serializer = serializer_class(singular_content)

        return Response(serializer.data)


class IntroContentSingular(SingularItemAPIView):
    queryset = IntroContent.objects.all()
    serializer_class = IntroContentSerializer


class AboutContentSingular(SingularItemAPIView):
    queryset = AboutContent.objects.all()
    serializer_class = AboutContentSerializer


class GoalContentSingular(SingularItemAPIView):
    queryset = GoalContent.objects.all()
    serializer_class = GoalContentSerializer


# Sponsor

class SponsorList(ListAPIView):
    serializer_class = SponsorSerializer
    queryset = Sponsor.objects.all()


class SponsorDetail(RetrieveAPIView):
    serializer_class = SponsorSerializer
    queryset = Sponsor.objects.all()


# Social

class SocialList(ListAPIView):
    serializer_class = SocialSerializer
    queryset = Social.objects.all()


class SocialDetail(RetrieveAPIView):
    serializer_class = SocialSerializer
    queryset = Social.objects.all()


# Social

class ActivityList(ListAPIView):
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()


class ActivityDetail(RetrieveAPIView):
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()


# ProjectArea

class ProjectAreaList(ListAPIView):
    serializer_class = ProjectAreaSerializer
    queryset = ProjectArea.objects.all()


class ProjectAreaDetail(RetrieveAPIView):
    serializer_class = ProjectAreaSerializer
    queryset = ProjectArea.objects.all()


# Project

class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = Project.LIMIT['default']
    max_limit = Project.LIMIT['max']

    limit_query_param = 'limit'


class ProjectPageNumberPagination(PageNumberPagination):
    page_size = Project.PAGE_SIZE['default']
    max_page_size = Project.PAGE_SIZE['max']

    page_query_param = 'page'


class ProjectFilter(django_filters.FilterSet):
    class Meta:
        model = Project
        fields = ['project_area', 'centres__city']


class ProjectList(ListAPIView):
    serializer_class = ProjectListSerializer

    pagination_class = ProjectPageNumberPagination

    filter_backends = (django_filters.DjangoFilterBackend,)
    filter_class = ProjectFilter

    @set_eager_loading
    def get_queryset(self):
        queryset = Project.objects.all()

        limit = self.request.query_params.get('limit', None)

        if limit is not None:
            self.pagination_class = ProjectLimitOffsetPagination

        return queryset


class ProjectDetail(RetrieveAPIView):
    serializer_class = ProjectDetailSerializer

    @set_eager_loading
    def get_queryset(self):
        return Project.objects.all()


# EventCategory

class EventCategoryList(ListAPIView):
    serializer_class = EventCategorySerializer
    queryset = EventCategory.objects.all()


class EventCategoryDetail(RetrieveAPIView):
    serializer_class = EventCategorySerializer
    queryset = EventCategory.objects.all()


# Event

class EventLimitOffsetPagination(LimitOffsetPagination):
    default_limit = Event.LIMIT['default']
    max_limit = Event.LIMIT['max']

    limit_query_param = 'limit'


class EventPageNumberPagination(PageNumberPagination):
    page_size = Event.PAGE_SIZE['default']
    max_page_size = Event.PAGE_SIZE['max']

    page_query_param = 'page'


class EventFilter(django_filters.FilterSet):
    class Meta:
        model = Event
        fields = ['event_category', 'project', 'centres__city']


class EventList(ListAPIView):
    serializer_class = EventListSerializer

    pagination_class = EventPageNumberPagination

    filter_backends = (django_filters.DjangoFilterBackend,)
    filter_class = EventFilter

    @set_eager_loading
    def get_queryset(self):
        queryset = Event.objects.all()

        limit = self.request.query_params.get('limit', None)

        if limit is not None:
            self.pagination_class = EventLimitOffsetPagination

        return queryset


class EventDetail(RetrieveAPIView):
    serializer_class = EventDetailSerializer

    @set_eager_loading
    def get_queryset(self):
        return Event.objects.all()


# City

class CityList(ListAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()


# Participant

class ParticipantList(ListAPIView):
    '''
    You can use `head_office` quary parameter to get only head office
    participants (with `centre` foreign key that equals `NULL`)
    '''
    serializer_class = ParticipantSerializer

    @set_eager_loading
    def get_queryset(self):
        queryset = Participant.objects.all()

        head_office = self.request.query_params.get('head_office', None)

        if head_office is not None:
            queryset = queryset.filter(centre__isnull=True)

        return queryset


# Contact

class ContactList(ListAPIView):
    '''
    You can use `head_office` quary parameter to get only head office
    contacts (with `centre` foreign key that equals `NULL`)
    '''
    serializer_class = ContactSerializer

    @set_eager_loading
    def get_queryset(self):
        queryset = Contact.objects.all()

        head_office = self.request.query_params.get('head_office', None)

        if head_office is not None:
            queryset = queryset.filter(centre__isnull=True)

        return queryset


class ContactDetail(RetrieveAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


# Centre

class CentreList(ListAPIView):
    '''
    You can use `related` quary parameter to specify singular relation that
    should be included in serialized objects list. Available options are:

    1. 'related=city', to include only nested city object
    '''
    serializer_class = CentreListSerializer

    @set_eager_loading
    def get_queryset(self):
        queryset = Centre.objects.all()

        related = self.request.query_params.get('related')

        if related == 'city':
            self.serializer_class = CentreCitySerializer

        return queryset


class CentreDetail(RetrieveAPIView):
    serializer_class = CentreDetailSerializer

    @set_eager_loading
    def get_queryset(self):
        return Centre.objects.all()


# CentreSubpage

class CentreSubpageFilter(django_filters.FilterSet):
    class Meta:
        model = CentreSubpage
        fields = ['centre__city']


class CentreSubpageList(ListAPIView):
    serializer_class = CentreSubpageSerializer

    filter_backends = (django_filters.DjangoFilterBackend,)
    filter_class = CentreSubpageFilter

    @set_eager_loading
    def get_queryset(self):
        return CentreSubpage.objects.all()


class CentreSubpageDetail(RetrieveAPIView):
    serializer_class = CentreSubpageSerializer

    @set_eager_loading
    def get_queryset(self):
        return CentreSubpage.objects.all()


# Worksheet

class WorksheetList(CreateModelMixin, GenericAPIView):
    serializer_class = WorksheetSerializer
    queryset = Worksheet.objects.all()

    def perform_create(self, serializer):
        '''
        Send an e-mail notification on succesfull serializer save
        '''
        serializer.save()
        serializer.send_email()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
