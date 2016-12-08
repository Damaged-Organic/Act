# diy_project/diy/subscription/urls_api.py
from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from .views_api import SubscriberCreate

urlpatterns = [
    url(
        r'^subscribers$',
        SubscriberCreate.as_view(),
        name='subscribers_create',
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
