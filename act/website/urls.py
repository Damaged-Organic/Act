# act_project/act/website/urls.py
from django.conf.urls import include, url

from . import views

app_name = 'website'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
