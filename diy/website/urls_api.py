# diy_project/diy/website/urls_api.py
from django.conf.urls import url

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from website.views_api import (
    api_root,
    SponsorList, SponsorDetail,
    SocialList, SocialDetail,
    ProjectAreaList, ProjectAreaDetail,
    ProjectList, ProjectDetail,
)

urlpatterns = [
    # Root
    url(r'^$', api_root),
    # Sponsor
    url(r'^sponsors$', SponsorList.as_view(), name='sponsors_list'),
    url(
        r'^sponsors/(?P<pk>[0-9]+)$',
        SponsorDetail.as_view(),
        name='sponsors_detail',
    ),
    # Social
    url(r'^socials$', SocialList.as_view(), name='socials_list'),
    url(
        r'^socials/(?P<pk>[0-9]+)$',
        SocialDetail.as_view(),
        name='socials_detail',
    ),
    # ProjectArea
    url(
        r'^projects_areas$',
        ProjectAreaList.as_view(),
        name='projects_areas_list',
    ),
    url(
        r'^projects_areas/(?P<pk>[0-9]+)$',
        ProjectAreaDetail.as_view(),
        name='projects_areas_detail',
    ),
    # Project
    url(r'^projects$', ProjectList.as_view(), name='projects_list'),
    url(
        r'^projects/(?P<pk>[0-9]+)$',
        ProjectDetail.as_view(),
        name='projects_detail',
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
