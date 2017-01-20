# act_project/act/metadata/views_api.py
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import get_object_or_404

from rest_framework.generics import (
    ListAPIView, RetrieveAPIView,
)

from .models import Metadata, OpenGraph, TwitterCard
from .serializers import (
    MetadataListSerializer, MetadataDetailSerializer,
)
from .utils import get_supported_model_instance


class MetadataList(ListAPIView):
    serializer_class = MetadataListSerializer
    queryset = Metadata.objects.all()


class MetadataDetail(RetrieveAPIView):
    serializer_class = MetadataDetailSerializer
    queryset = Metadata.objects.all()
    lookup_field = 'url_name'

    def get_object(self):
        metadata = super(MetadataDetail, self).get_object()

        metadata.provide_open_graph(
            open_graph_type=OpenGraph.TYPE_WEBSITE)
        metadata.provide_twitter_card(
            twitter_card=TwitterCard.CARD_SUMMARY)

        return metadata


class MetadataDetailOnObject(RetrieveAPIView):
    serializer_class = MetadataDetailSerializer
    queryset = Metadata.objects.all()
    lookup_field = 'url_name'

    def get_object(self):
        master_metadata = super(MetadataDetailOnObject, self).get_object()

        try:
            instance = get_supported_model_instance(
                self.kwargs['url_name'], self.kwargs['id'])
        except (KeyError, ObjectDoesNotExist):
            raise Http404('Cannot load required object')

        metadata = Metadata.build_metadata_from_dict(
            master_metadata, instance.get_metadata())

        metadata.provide_open_graph(
            open_graph_type=OpenGraph.TYPE_ARTICLE)
        metadata.provide_twitter_card(
            twitter_card=TwitterCard.CARD_SUMMARY_LARGE_IMAGE)

        return metadata
