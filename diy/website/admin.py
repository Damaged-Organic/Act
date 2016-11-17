# diy_project/diy/website/admin.py
from django import forms
from django.db import models
from django.contrib import admin
from django.utils.html import escape

from transmeta import canonical_fieldname

from diy.admin import (
    admin_site, DefaultOrderingModelAdmin,
    ForbidAddMixin, ForbidDeleteMixin, ContentBlockMixin,
)

from .models import (
    IntroContent,
    ProjectArea, Project,
    EventCategory, Event,
    City,
    Centre, CentreSubpage, Participant, Contact,
)


# Content

@admin.register(IntroContent, site=admin_site)
class IntroContentAdmin(
    ForbidAddMixin, ForbidDeleteMixin, DefaultOrderingModelAdmin
):
    list_display = ('headline_uk', )

    fieldsets = (
        ('Локалізована інформація', {
            'fields': ('headline_uk', ),
        }),
    )

    formfield_overrides = {
        models.CharField: {'widget': forms.TextInput(attrs={
            'style': 'width:50%; max-width:50%;'
        })},
    }


# Project

@admin.register(ProjectArea, site=admin_site)
class ProjectAreaAdmin(DefaultOrderingModelAdmin):
    list_display = ('id', 'title', 'projects_count', )
    list_display_links = ('title', )

    fieldsets = (
        ('Локалізована інформація', {
            'fields': ('title_uk', ),
        }),
    )


@admin.register(Project, site=admin_site)
class ProjectAdmin(DefaultOrderingModelAdmin):
    list_display = ('id', 'title', 'started_at', 'project_area', )
    list_display_links = ('title', )

    fieldsets = (
        (None, {
            'fields': ('image', 'project_area', ),
        }),
        ('Локалізована інформація', {
            'fields': ('title_uk', 'short_description_uk', ),
        }),
    )

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(ProjectAdmin, self).formfield_for_dbfield(
            db_field, **kwargs
        )
        db_fieldname = canonical_fieldname(db_field)

        if db_fieldname == 'title':
            field.widget = forms.TextInput(attrs={
                'style': 'width:50%; max-width:50%;'
            })

        if db_fieldname == 'short_description':
            field.widget = forms.Textarea(attrs={
                'style': 'resize:none', 'cols': '100', 'rows': '5'
            })

        return field


# Event

@admin.register(EventCategory, site=admin_site)
class EventCategoryAdmin(DefaultOrderingModelAdmin):
    list_display = ('id', 'title', 'events_count', )
    list_display_links = ('title', )

    fieldsets = (
        ('Локалізована інформація', {
            'fields': ('title_uk', ),
        }),
    )


@admin.register(Event, site=admin_site)
class EventAdmin(DefaultOrderingModelAdmin):
    list_display = ('id', 'title', 'created_at', 'event_category', )
    list_display_links = ('title', )

    fieldsets = (
        (None, {
            'fields': ('image', 'event_category', ),
        }),
        ('Локалізована інформація', {
            'fields': ('title_uk', 'short_description_uk', ),
        }),
    )

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(EventAdmin, self).formfield_for_dbfield(
            db_field, **kwargs
        )
        db_fieldname = canonical_fieldname(db_field)

        if db_fieldname == 'title':
            field.widget = forms.TextInput(attrs={
                'style': 'width:50%; max-width:50%;'
            })

        if db_fieldname == 'short_description':
            field.widget = forms.Textarea(attrs={
                'style': 'resize:none', 'cols': '100', 'rows': '5'
            })

        return field


# City

@admin.register(City, site=admin_site)
class CityAdmin(DefaultOrderingModelAdmin):
    list_display = ('id', 'name', 'centre', )
    list_display_links = ('name', )

    fieldsets = (
        (None, {
            'fields': ('photo', 'centre', ),
        }),
        ('Локалізована інформація', {
            'fields': ('name_uk', ),
        }),
    )

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(CityAdmin, self).formfield_for_dbfield(
            db_field, **kwargs
        )
        db_fieldname = canonical_fieldname(db_field)

        if db_fieldname == 'name':
            field.widget = forms.TextInput(attrs={
                'style': 'width:50%; max-width:50%;'
            })

        return field
