# act_project/act/subscription/admin.py
from django import forms
from django.contrib import admin

from act.services.transmeta import canonical_fieldname

from act.admin import (
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
