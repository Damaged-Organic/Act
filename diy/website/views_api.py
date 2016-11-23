# diy_project/diy/website/views_api.py
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from .models import (
    Sponsor, Social,
    ProjectArea, Project,
)
from .serializers import (
    SponsorSerializer, SocialSerializer,
    ProjectAreaSerializer, ProjectSerializer,
)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'sponsors': reverse('sponsors_list', request=request, format=format),
        'socials': reverse('socials_list', request=request, format=format),
        'projects_areas': reverse(
            'projects_areas_list', request=request, format=format
        ),
        'projects': reverse('projects_list', request=request, format=format),
    })


class SponsorList(APIView):
    def get(self, request, format=None):
        sponsors = Sponsor.objects.all()
        serializer = SponsorSerializer(sponsors, many=True)

        return Response(serializer.data)


class SponsorDetail(APIView):
    def get_object(self, pk):
        try:
            return Sponsor.objects.get(pk=pk)
        except Sponsor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        sponsor = self.get_object(pk)
        serializer = SponsorSerializer(sponsor)

        return Response(serializer.data)


class SocialList(APIView):
    def get(self, request, format=None):
        socials = Social.objects.all()
        serializer = SocialSerializer(socials, many=True)

        return Response(serializer.data)


class SocialDetail(APIView):
    def get_object(self, pk):
        try:
            return Social.objects.get(pk=pk)
        except Social.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        social = self.get_object(pk)
        serializer = SocialSerializer(social)

        return Response(serializer.data)


class ProjectAreaList(APIView):
    def get(self, request, format=None):
        projects_areas = ProjectArea.objects.all()
        serializer = ProjectAreaSerializer(projects_areas, many=True)

        return Response(serializer.data)


class ProjectAreaDetail(APIView):
    def get_object(self, pk):
        try:
            return ProjectArea.objects.get(pk=pk)
        except ProjectArea.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        project_area = self.get_object(pk)
        serializer = ProjectAreaSerializer(project_area)

        return Response(serializer.data)


class ProjectList(APIView):
    def get(self, request, format=None):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)

        return Response(serializer.data)


class ProjectDetail(APIView):
    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project)

        return Response(serializer.data)

'''
from rest_framework import mixins
from rest_framework import generics

class SponsorList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class SponsorDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

-OR-

class SponsorList(generics.ListAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer


class SponsorDetail(generics.RetrieveAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
'''
