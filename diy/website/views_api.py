# diy_project/diy/website/views_api.py
from rest_framework import viewsets

from .models import Sponsor, Social
from .serializers import SponsorSerializer, SocialSerializer


class SponsorViewSet(viewsets.ModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer


class SocialViewSet(viewsets.ModelViewSet):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer
