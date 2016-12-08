# diy_project/diy/metadata/views_api.py
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView,
)

from .models import Metadata
from .serializers import MetadataSerializer


class MetadataList(ListAPIView):
    serializer_class = MetadataSerializer
    queryset = Metadata.objects.all()


class MetadataDetail(RetrieveAPIView):
    serializer_class = MetadataSerializer
    queryset = Metadata.objects.all()
