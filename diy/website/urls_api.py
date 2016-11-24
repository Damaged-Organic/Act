# diy_project/diy/website/urls_api.py
from django.conf.urls import url

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from website.views_api import (
    api_root,
    IntroContentSingular,
    SponsorList, SponsorDetail,
    SocialList, SocialDetail,
    ProjectAreaList, ProjectAreaDetail,
    ProjectList, ProjectDetail,
    EventCategoryList, EventCategoryDetail,
    EventList, EventDetail,
)

urlpatterns = [
    # Root
    url(r'^$', api_root),
    # IntroContent
    url(
        r'^intro_content$',
        IntroContentSingular.as_view(),
        name='intro_content_singular'
    ),
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
    # EventCategory
    url(
        r'^events_categories$',
        EventCategoryList.as_view(),
        name='events_categories_list',
    ),
    url(
        r'^events_categories/(?P<pk>[0-9]+)$',
        EventCategoryDetail.as_view(),
        name='events_categories_detail',
    ),
    # Event
    url(r'^events$', EventList.as_view(), name='events_list'),
    url(
        r'^events/(?P<pk>[0-9]+)$',
        EventDetail.as_view(),
        name='events_detail',
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
