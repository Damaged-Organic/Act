# diy_project/diy/metadata/urls_api.py
from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from .views_api import (
    MetadataList, MetadataDetail,
)

urlpatterns = [
    url(r'^metadata$', MetadataList.as_view(), name='metadata_list'),
    url(
        r'^metadata/(?P<pk>[0-9]+)$',
        MetadataDetail.as_view(),
        name='metadata_detail',
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
