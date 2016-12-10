# diy_project/diy/subscription/urls_api.py
from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from .views_api import SubscriberList, SubscriberDetail

urlpatterns = [
    url(r'^subscribers$', SubscriberList.as_view(), name='subscribers_list'),
    url(r'^subscribers/(?P<pk>[0-9]+)$',
        SubscriberDetail.as_view(),
        name='subscribers_detail'),
    url(r'^subscribers/subscribe/'
        r'(?P<pk>[0-9]+)/(?P<checkout_hash>[a-f0-9]+)$',
        SubscriberDetail.as_view(),
        name='subscribers_detail_subscribe'),
    url(r'^subscribers/unsubscribe/'
        r'(?P<pk>[0-9]+)/(?P<checkout_hash>[a-f0-9]+)$',
        SubscriberDetail.as_view(),
        name='subscribers_detail_unsubscribe'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
