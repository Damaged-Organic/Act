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
    Sponsor, Social,
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


# Links

@admin.register(Sponsor, site=admin_site)
class SponsorAdmin(
    ForbidAddMixin, ForbidDeleteMixin, DefaultOrderingModelAdmin
):
    readonly_fields = ('logo_preview', )
    list_display = ('title_uk', 'link', )

    fieldsets = (
        (None, {
            'fields': ('logo_preview', 'link', ),
        }),
        ('Локалізована інформація', {
            'fields': ('title_uk', ),
        }),
    )

    formfield_overrides = {
        models.CharField: {'widget': forms.TextInput(attrs={
            'style': 'width:50%; max-width:50%;'
        })},
    }


@admin.register(Social, site=admin_site)
class SocialAdmin(
    ForbidAddMixin, ForbidDeleteMixin, DefaultOrderingModelAdmin
):
    readonly_fields = ('icon', )
    list_display = ('title', 'link', )

    fieldsets = (
        (None, {
            'fields': ('link', 'title', ),
        }),
    )

    formfield_overrides = {
        models.CharField: {'widget': forms.TextInput(attrs={
            'style': 'width:25%; max-width:25%;'
        })},
    }


# Project

@admin.register(ProjectArea, site=admin_site)
class ProjectAreaAdmin(DefaultOrderingModelAdmin):
    list_display = ('id', 'title_uk', 'get_projects_count', )
    list_display_links = ('title_uk', )

    fieldsets = (
        ('Локалізована інформація', {
            'fields': ('title_uk', ),
        }),
    )


@admin.register(Project, site=admin_site)
class ProjectAdmin(DefaultOrderingModelAdmin):
    list_display = (
        'id', 'title_uk', 'started_at', 'project_area', 'is_active',
    )
    list_display_links = ('title_uk', )

    fieldsets = (
        (None, {
            'fields': ('image', 'project_area', 'is_active', ),
        }),
        ('Локалізована інформація', {
            'fields': ('title_uk', 'short_description_uk', 'content_uk', ),
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
    list_display = ('id', 'title_uk', 'get_events_count', )
    list_display_links = ('title_uk', )

    fieldsets = (
        ('Локалізована інформація', {
            'fields': ('title_uk', ),
        }),
    )


@admin.register(Event, site=admin_site)
class EventAdmin(DefaultOrderingModelAdmin):
    list_display = (
        'id', 'title_uk', 'created_at', 'event_category', 'is_active',
    )
    list_display_links = ('title_uk', )

    fieldsets = (
        (None, {
            'fields': ('image', 'event_category', 'is_active', ),
        }),
        ('Локалізована інформація', {
            'fields': ('title_uk', 'short_description_uk', 'content_uk', ),
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
    list_display = ('id', 'name_uk', )
    list_display_links = ('name_uk', )

    fieldsets = (
        (None, {
            'fields': ('photo', ),
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


# Centre

@admin.register(Centre, site=admin_site)
class CentreAdmin(DefaultOrderingModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('city', 'projects', 'events', ),
        }),
    )
