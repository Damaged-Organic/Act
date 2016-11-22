# diy_project/diy/website/urls_api.py
from django.conf.urls import url
from rest_framework import routers

from .views_api import SponsorViewSet, SocialViewSet

router = routers.DefaultRouter()
router.register(r'sponsors', SponsorViewSet)
router.register(r'socials', SocialViewSet)

urlpatterns = router.urls
