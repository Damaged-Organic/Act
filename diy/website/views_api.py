# diy_project/diy/website/views_api.py
from django.http import Http404

from rest_framework.response import Response
from rest_framework.generics import (
    GenericAPIView, ListAPIView, RetrieveAPIView,
)
from rest_framework.pagination import (
    LimitOffsetPagination, PageNumberPagination,
)
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from django_filters import rest_framework as django_filters

from .models import (
    IntroContent,
    Sponsor, Social,
    ProjectArea, Project,
    EventCategory, Event,
)
from .serializers import (
    IntroContentSerializer,
    SponsorSerializer, SocialSerializer,
    ProjectAreaSerializer, ProjectSerializer,
    EventCategorySerializer, EventSerializer,
)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'intro_content': reverse(
            'intro_content_singular', request=request, format=format
        ),
        'sponsors': reverse('sponsors_list', request=request, format=format),
        'socials': reverse('socials_list', request=request, format=format),
        'projects_areas': reverse(
            'projects_areas_list', request=request, format=format
        ),
        'projects': reverse('projects_list', request=request, format=format),
        'events_categories': reverse(
            'events_categories_list', request=request, format=format
        ),
        'events': reverse('events_list', request=request, format=format),
    })


# IntroContent

class IntroContentSingular(GenericAPIView):
    '''
    This view is tricky, as it overrides common behavior of `get_object()`
    method. It does not require positional `pk` argument, because it's
    intention is to return first & only one object of a given queryset
    '''
    queryset = IntroContent.objects.all()
    serializer_class = IntroContentSerializer

    def get_object(self):
        instance = self.get_queryset().first()
        return instance

    def get(self, request):
        intro_content = self.get_object()

        if not intro_content:
            raise Http404

        serializer = IntroContentSerializer(intro_content)
        return Response(serializer.data)


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


# ProjectArea

class ProjectAreaList(ListAPIView):
    serializer_class = ProjectAreaSerializer
    queryset = ProjectArea.objects.all()


class ProjectAreaDetail(RetrieveAPIView):
    serializer_class = ProjectAreaSerializer
    queryset = ProjectArea.objects.all()


# Project

class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 3
    limit_query_param = 'limit'
    max_limit = 100


class ProjectPageNumberPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page'
    max_page_size = 100


class ProjectFilter(django_filters.FilterSet):
    class Meta:
        model = Project
        fields = ['project_area']


class ProjectList(ListAPIView):
    serializer_class = ProjectSerializer

    pagination_class = ProjectPageNumberPagination

    filter_backends = (django_filters.DjangoFilterBackend,)
    filter_class = ProjectFilter

    def get_queryset(self):
        queryset = Project.objects.order_by('-started_at')

        limit = self.request.query_params.get('limit', None)

        if limit is not None:
            self.pagination_class = ProjectLimitOffsetPagination

        return queryset


class ProjectDetail(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


# EventCategory

class EventCategoryList(ListAPIView):
    serializer_class = EventCategorySerializer
    queryset = EventCategory.objects.all()


class EventCategoryDetail(RetrieveAPIView):
    serializer_class = EventCategorySerializer
    queryset = EventCategory.objects.all()


# Event

class EventLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 3
    limit_query_param = 'limit'
    max_limit = 100


class EventPageNumberPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page'
    max_page_size = 100


class EventFilter(django_filters.FilterSet):
    class Meta:
        model = Event
        fields = ['event_category', 'project']


class EventList(ListAPIView):
    serializer_class = EventSerializer

    pagination_class = EventPageNumberPagination

    filter_backends = (django_filters.DjangoFilterBackend,)
    filter_class = EventFilter

    def get_queryset(self):
        queryset = Event.objects.order_by('-created_at')

        limit = self.request.query_params.get('limit', None)

        if limit is not None:
            self.pagination_class = EventLimitOffsetPagination

        return queryset


class EventDetail(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
