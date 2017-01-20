# act_project/act/metadata/urls_api.py
from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from .views_api import (
    MetadataList, MetadataDetail, MetadataDetailOnObject,
)

urlpatterns = [
    url(r'^metadata$', MetadataList.as_view(), name='metadata_list'),
    url(
        r'^metadata/(?P<url_name>[a-z_]+)$',
        MetadataDetail.as_view(),
        name='metadata_detail',
    ),
    url(
        r'^metadata/(?P<url_name>[a-z_]+)/(?P<id>[0-9]+)$',
        MetadataDetailOnObject.as_view(),
        name='metadata_detail_on_object',
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
