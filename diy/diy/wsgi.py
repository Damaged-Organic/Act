# diy_project/diy/diy/wsgi.py
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "diy.settings.prod")

application = get_wsgi_application()
