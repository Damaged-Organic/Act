# act_project/act/website/admin.py
from django import forms
from django.db import models
from django.contrib import admin
from django.utils.html import escape
from django.contrib.admin.widgets import ForeignKeyRawIdWidget

# Notice overridden transmeta import!
from act.services.transmeta import canonical_fieldname

from act.admin import (
    admin_site, DefaultOrderingModelAdmin,
    ForbidAddMixin, ForbidDeleteMixin,
)

from .models import (
    IntroContent,
    Sponsor, Social, Activity,
    ProjectAttachedDocument, EventAttachedDocument,
    ProjectArea, Project,
    EventCategory, Event,
    City,
    Centre, CentreSubpage, Participant, Contact,
    Worksheet,
    top_event_validator,
)


# Content

@admin.register(IntroContent, site=admin_site)
class IntroContentAdmin(
    ForbidAddMixin, ForbidDeleteMixin, DefaultOrderingModelAdmin
):
    list_display = ('headline_uk', )

    fieldsets = (
        (None, {
            'fields': ('logo_preview', ),
        }),
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
            'fields': ('logo_preview', 'logo', 'link', ),
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


# Activity

@admin.register(Activity, site=admin_site)
class ActivityAdmin(
    ForbidAddMixin, ForbidDeleteMixin, DefaultOrderingModelAdmin
):
    readonly_fields = ('icon', )
    list_display = ('title_uk', )

    fieldsets = (
        ('Локалізована інформація', {
            'fields': ('title_uk', ),
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


class ProjectCentresInline(admin.TabularInline):
    model = Centre.projects.through
    extra = 1

    def to_string(self):
        return self.centre.city.name

    Centre.projects.through.__str__ = to_string
    Centre.projects.through._meta.verbose_name_plural = "Належність до центрів"


class ProjectAttachedDocumentInline(admin.TabularInline):
    model = ProjectAttachedDocument
    fields = ('description_uk', 'document', )
    extra = 1


@admin.register(Project, site=admin_site)
class ProjectAdmin(DefaultOrderingModelAdmin):
    readonly_fields = ('image_preview', )
    list_display = (
        'id', 'title_uk', 'started_at', 'project_area', 'is_active',
    )
    list_display_links = ('title_uk', )

    fieldsets = (
        (None, {
            'fields': (
                'image_preview', 'image', 'project_area', 'is_active',
            ),
        }),
        ('Локалізована інформація', {
            'fields': ('title_uk', 'content_uk', ),
        }),
    )

    inlines = [
        ProjectCentresInline, ProjectAttachedDocumentInline,
    ]

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(ProjectAdmin, self).formfield_for_dbfield(
            db_field, **kwargs
        )
        db_fieldname = canonical_fieldname(db_field)

        if db_fieldname == 'title':
            field.widget = forms.TextInput(attrs={
                'style': 'width:50%; max-width:50%;'
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


class EventCentresInline(admin.TabularInline):
    model = Centre.events.through
    extra = 1

    def to_string(self):
        return self.centre.city.name

    Centre.events.through.__str__ = to_string
    Centre.events.through._meta.verbose_name_plural = "Належність до центрів"


class EventAttachedDocumentInline(admin.TabularInline):
    model = EventAttachedDocument
    fields = ('description_uk', 'document', )
    extra = 1


@admin.register(Event, site=admin_site)
class EventAdmin(DefaultOrderingModelAdmin):
    readonly_fields = ('image_preview', )
    list_display = (
        'id', 'title_uk', 'created_at', 'event_category', 'is_active',
    )
    list_display_links = ('title_uk', )
    raw_id_fields = ('project', )

    fieldsets = (
        (None, {
            'fields': (
                'image_preview', 'image',
                'event_category', 'project', 'is_active',
            ),
        }),
        ('Локалізована інформація', {
            'fields': ('title_uk', 'content_uk', ),
        }),
    )

    inlines = [
        EventCentresInline, EventAttachedDocumentInline,
    ]

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
class CityAdmin(
    ForbidAddMixin, ForbidDeleteMixin, DefaultOrderingModelAdmin
):
    readonly_fields = ('name_uk', 'photo_preview', )
    list_display = ('id', 'name_uk', )
    list_display_links = ('name_uk', )

    fieldsets = (
        (None, {
            'fields': ('photo_preview', 'photo', ),
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


# Participant

class ParticipantInline(admin.TabularInline):
    model = Participant
    fields = ('name_uk', 'surname_uk', 'position_uk', 'photo', )
    extra = 0
    show_change_link = True

    '''
    Custom template to display enumerated tabular inline
    '''
    template = "admin/inlines/tabular_enumerated.html"


@admin.register(Participant, site=admin_site)
class ParticipantAdmin(DefaultOrderingModelAdmin):
    readonly_fields = ('photo_preview', )
    list_display = ('id', 'get_full_name', 'position_uk', 'centre', )
    list_display_links = ('get_full_name', )

    fieldsets = (
        (None, {
            'fields': ('photo_preview', 'photo', 'centre', ),
        }),
        ('Локалізована інформація', {
            'fields': ('name_uk', 'surname_uk', 'position_uk', ),
        }),
    )


# Contact

class ContactInline(admin.StackedInline):
    model = Contact
    fields = (('email', 'phone', 'address_uk',), )
    can_delete = False


class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['centre'].empty_label = 'Центральний офіс'


@admin.register(Contact, site=admin_site)
class ContactAdmin(
    ForbidAddMixin, ForbidDeleteMixin, DefaultOrderingModelAdmin
):
    form = ContactForm

    list_display = ('centre_view', 'email', 'phone', 'address_uk', )
    list_display_links = ('centre_view', )

    fieldsets = (
        (None, {
            'fields': ('centre', 'email', 'phone', ),
        }),
        ('Локалізована інформація', {
            'fields': ('address_uk', ),
        }),
    )

    '''
    This is the only option to make field `readonly` while
    overriding it's attributes inside form class
    '''
    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(ContactAdmin, self).formfield_for_dbfield(
            db_field, **kwargs
        )
        db_fieldname = canonical_fieldname(db_field)

        if db_fieldname == 'centre':
            field.widget = forms.Select(attrs={
                'readonly': True, 'disabled': 'disabled',
            })

        return field

    '''
    This is used to specify empty value for an admin list view
    '''
    def centre_view(self, instance):
        return instance.centre
    centre_view.empty_value_display = 'Центральний офіс'


# Centre


class TopEventRawIdWidget(ForeignKeyRawIdWidget):
    def url_parameters(self):
        res = super(TopEventRawIdWidget, self).url_parameters()
        res["centres__in"] = self.form_instance.instance.id

        return res


class CentreAdminForm(forms.ModelForm):
    top_event = forms.ModelChoiceField(
        queryset=Event.objects.all(),
        widget=TopEventRawIdWidget(
            Centre._meta.get_field('top_event').rel, admin_site)
    )

    def __init__(self, *args, **kwargs):
        super(CentreAdminForm, self).__init__(*args, **kwargs)
        self.fields['top_event'].widget.form_instance = self
        self.fields['top_event'].label = (
            self._meta.model.top_event.field.verbose_name)

    def clean(self):
        cleaned_data = super(CentreAdminForm, self).clean()

        error_top_event = top_event_validator(
            cleaned_data.get('top_event'), cleaned_data.get('events'))
        if error_top_event:
            self.add_error('top_event', error_top_event)

        return cleaned_data


@admin.register(Centre, site=admin_site)
class CentreAdmin(
    ForbidAddMixin, ForbidDeleteMixin, DefaultOrderingModelAdmin
):
    form = CentreAdminForm

    readonly_fields = (
        'get_projects_count', 'get_events_count', 'get_participants_count',
    )
    list_display = (
        'city',
        'get_projects_count', 'get_events_count', 'get_participants_count',
    )
    list_display_links = ('city', )
    filter_horizontal = ('projects', 'events', )
    fieldsets = (
        (None, {
            'fields': (
                'city', 'short_description_uk',
                'projects', 'events', 'top_event',
            ),
        }),
    )
    raw_id_fields = ('top_event', )

    inlines = [
        ContactInline, ParticipantInline,
    ]

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(CentreAdmin, self).formfield_for_dbfield(
            db_field, **kwargs
        )
        db_fieldname = canonical_fieldname(db_field)

        if db_fieldname == 'short_description':
            field.widget = forms.Textarea(attrs={
                'style': 'resize:none', 'cols': '95', 'rows': '10'
            })

        return field


# Worksheet

@admin.register(Worksheet, site=admin_site)
class WorksheetAdmin(DefaultOrderingModelAdmin):
    pass
