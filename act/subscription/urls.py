# act_project/act/subscription/urls.py
from django.conf.urls import url

from .views_api import SubscriberDetail

urlpatterns = [
    url(r'^subscribers/subscribe/'
        r'(?P<pk>[0-9]+)/(?P<checkout_hash>[a-f0-9]+)$',
        SubscriberDetail.as_view(),
        name='subscribers_detail_subscribe_client'),
    url(r'^subscribers/unsubscribe/'
        r'(?P<pk>[0-9]+)/(?P<checkout_hash>[a-f0-9]+)$',
        SubscriberDetail.as_view(),
        name='subscribers_detail_unsubscribe_client'),
]
