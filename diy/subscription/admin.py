# diy_project/diy/subscription/admin.py
from django import forms
from django.contrib import admin

from diy.services.transmeta import canonical_fieldname

from diy.admin import (
    admin_site, DefaultOrderingModelAdmin,
    ForbidAddMixin,
)

from .models import Subscriber


@admin.register(Subscriber, site=admin_site)
class SubscriberAdmin(ForbidAddMixin, DefaultOrderingModelAdmin):
    readonly_fields = ('email', 'subscribed_at', )
    fieldsets = (
        (None, {
            'fields': ('email', 'subscribed_at', 'is_active', ), }),
    )
