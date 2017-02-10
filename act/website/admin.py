# act_project/act/website/admin.py
from django import forms
from django.db import models
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.contrib.admin.widgets import ForeignKeyRawIdWidget

# Notice overridden transmeta import!
from act.services.transmeta import canonical_fieldname

from act.admin import (
    admin_site, DefaultOrderingModelAdmin,
    ForbidAddMixin, ForbidDeleteMixin,
)

from .models import (
    IntroContent, AboutContent, GoalContent, DisclaimerContent,
    Sponsor, Social, Activity, Partner,
    ProjectAttachedDocument, EventAttachedDocument,
    ProjectArea, Project,
    EventCategory, Event,
    City,
    Centre, CentreSubpage, Participant, Contact,
    Worksheet,
)
from .validators import top_event_validator


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


@admin.register(AboutContent, site=admin_site)
class AboutContentAdmin(
    ForbidAddMixin, ForbidDeleteMixin, DefaultOrderingModelAdmin
):
    list_display = ('title_uk', )

    fieldsets = (
        ('Локалізована інформація', {
            'fields': ('title_uk', 'text_uk', ),
        }),
    )

    formfield_overrides = {
        models.CharField: {'widget': forms.TextInput(attrs={
            'style': 'width:35%; max-width:35%;'
        })},
    }


@admin.register(GoalContent, site=admin_site)
class GoalContentAdmin(
    ForbidAddMixin, ForbidDeleteMixin, DefaultOrderingModelAdmin
):
    list_display = ('title_uk', )

    fieldsets = (
        ('Локалізована інформація', {
            'fields': ('title_uk', 'text_uk', ),
        }),
    )

    formfield_overrides = {
        models.CharField: {'widget': forms.TextInput(attrs={
            'style': 'width:35%; max-width:35%;'
        })},
    }


@admin.register(DisclaimerContent, site=admin_site)
class DisclaimerContentAdmin(
    ForbidAddMixin, ForbidDeleteMixin, DefaultOrderingModelAdmin
):
    list_display = ('title', )

    fieldsets = (
        ('Локалізована інформація', {
            'fields': ('title', 'text_uk', 'text_en', ),
        }),
    )

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(DisclaimerContentAdmin, self).formfield_for_dbfield(
            db_field, **kwargs
        )
        db_fieldname = canonical_fieldname(db_field)

        if db_fieldname == 'title':
            field.widget = forms.TextInput(attrs={
                'style': 'width:45%; max-width:45%;',
            })

        if db_fieldname in ['text_uk', 'text_en']:
            field.widget = forms.Textarea(attrs={
                'style': 'resize:none', 'cols': '100', 'rows': '5',
            })

        return field


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

    def logo_preview(self, instance):
        return format_html(
            '<img src="{}" width="100" max-width="100">'
            .format(instance.logo.url))
    logo_preview.short_description = 'Логотип'


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


# Partner

@admin.register(Partner, site=admin_site)
class PartnerAdmin(DefaultOrderingModelAdmin):
    readonly_fields = ('logo_preview', )
    list_display = ('name_uk', 'link', )

    fieldsets = (
        (None, {
            'fields': ('logo_preview', 'logo', 'link', ),
        }),
        ('Локалізована інформація', {
            'fields': ('name_uk', ),
        }),
    )

    formfield_overrides = {
        models.CharField: {'widget': forms.TextInput(attrs={
            'style': 'width:50%; max-width:50%;'
        })},
    }

    def logo_preview(self, instance):
        return format_html(
            '<img src="{}" width="200" max-width="200">'
            .format(instance.logo.url))
    logo_preview.short_description = 'Логотип'


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


class ProjectAdminForm(forms.ModelForm):
    events = forms.ModelMultipleChoiceField(
        queryset=Event.objects.all(), required=False)

    def __init__(self, *args, **kwargs):
        super(ProjectAdminForm, self).__init__(*args, **kwargs)

        self.fields['events'].initial = self.instance.events.all()
        self.fields['events'].label = (
            self._meta.model.events.rel.related_model
                ._meta.verbose_name_plural)
        self.fields['events'].help_text = (
            "Ви можете обрати декілька матеріалів "
            "одразу, затиснувши клавішу 'Ctrl'")

    def save(self, *args, **kwargs):
        instance = super(ProjectAdminForm, self).save(commit=False)

        # `save()` on Model after ModelForm `save(commit=False)` provides
        # required `save_m2m()` method to ModelForm subclass itself
        instance.save()

        self.fields['events'].initial.update(project=None)
        self.cleaned_data['events'].update(project=instance)

        return instance


@admin.register(Project, site=admin_site)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm

    ordering = ('-modified_at',)
    readonly_fields = ('image_preview', )
    list_display = (
        'id', 'title_uk', 'started_at', 'modified_at', 'project_area',
        'is_active',
    )
    list_display_links = ('title_uk', )

    fieldsets = (
        (None, {
            'fields': (
                'image_preview', 'image', 'project_area', 'is_active',
                'events', 'modified_at',
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

    def image_preview(self, instance):
        return format_html(
            '<img src="{}" width="300" max-width="300">'
            .format(instance.image.url))
    image_preview.short_description = 'Превʼю головного зображення'


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
class EventAdmin(admin.ModelAdmin):
    ordering = ('-created_at', )
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

    def image_preview(self, instance):
        return format_html(
            '<img src="{}" width="300" max-width="300">'
            .format(instance.image.url))
    image_preview.short_description = 'Превʼю головного зображення'


# City

class CityAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CityAdminForm, self).__init__(*args, **kwargs)

        self.fields['photo'].help_text = (
            "Рекомендований розмір фотографії - 1920х1280 пікселів")
        self.fields['photo_square'].help_text = (
            "Рекомендований розмір фотографії - 480х480 пікселів")
        self.fields['photo_high'].help_text = (
            "Рекомендований розмір фотографії - 400х1280 пікселів")


@admin.register(City, site=admin_site)
class CityAdmin(
    ForbidAddMixin, ForbidDeleteMixin, DefaultOrderingModelAdmin
):
    form = CityAdminForm

    readonly_fields = (
        'name_uk',
        'photo_preview',
        'photo_square_preview',
        'photo_high_preview', )

    list_display = ('id', 'name_uk', )
    list_display_links = ('name_uk', )

    fieldsets = (
        (None, {
            'fields': (
                'photo_preview', 'photo',
                'photo_square_preview', 'photo_square',
                'photo_high_preview', 'photo_high', ),
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

    def photo_preview(self, instance):
        return format_html(
            '<img src="{}" width="400" max-width="400">'
            .format(instance.photo.url))
    photo_preview.short_description = 'Превʼю головної фотографії'

    def photo_square_preview(self, instance):
        return format_html(
            '<img src="{}" width="300" max-width="300">'
            .format(instance.photo_square.url))
    photo_square_preview.short_description = 'Превʼю квадратної фотографії'

    def photo_high_preview(self, instance):
        return format_html(
            '<img src="{}" height="200" max-height="200">'
            .format(instance.photo_high.url))
    photo_high_preview.short_description = 'Превʼю високої фотографії'


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

    def photo_preview(self, instance):
        return format_html(
            '<img src="{}" width="200" max-width="200">'
            .format(instance.photo.url))
    photo_preview.short_description = 'Превʼю фотографії'


# Contact

class ContactInline(admin.TabularInline):
    model = Contact
    fields = ('email', 'phone', 'address_uk', 'social_link', )
    can_delete = False


@admin.register(Contact, site=admin_site)
class ContactAdmin(
    ForbidAddMixin, ForbidDeleteMixin, DefaultOrderingModelAdmin
):
    readonly_fields = ('centre_view', )
    list_display = ('centre_view', 'email', 'phone', 'address_uk', )
    list_display_links = ('centre_view', )

    fieldsets = (
        (None, {
            'fields': ('centre_view', 'email', 'phone', 'social_link', ),
        }),
        ('Локалізована інформація', {
            'fields': ('address_uk', ),
        }),
    )

    '''
    This is used to specify empty value for an admin list view
    '''
    def centre_view(self, instance):
        return instance.centre if instance.centre else 'Центральний офіс'
    centre_view.short_description = Centre._meta.verbose_name


# Centre


class TopEventRawIdWidget(ForeignKeyRawIdWidget):
    def url_parameters(self):
        res = super(TopEventRawIdWidget, self).url_parameters()
        res["centres__in"] = self.form_instance.instance.id

        return res


class CentreSubpageInline(
    ForbidAddMixin, ForbidDeleteMixin, admin.TabularInline
):
    model = CentreSubpage
    readonly_fields = ('headline_uk', 'content_preview', )
    fields = ('headline_uk', 'content_preview', )
    extra = 0
    show_change_link = True
    can_delete = False

    '''
    Custom template to display linked tabular inline
    '''
    template = "admin/inlines/tabular_linked.html"


class CentreAdminForm(forms.ModelForm):
    top_event = forms.ModelChoiceField(
        required=False,
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
        ContactInline, ParticipantInline, CentreSubpageInline,
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


# CentreSubpage

@admin.register(CentreSubpage, site=admin_site)
class CentreSubpageAdmin(
    ForbidAddMixin, ForbidDeleteMixin, DefaultOrderingModelAdmin
):
    list_display = ('id', 'headline_uk', 'centre', )
    list_display_links = ('headline_uk', )

    readonly_fields = ('centre_preview', )

    fieldsets = (
        (None, {
            'fields': ('centre_preview', ),
        }),
        ('Локалізована інформація', {
            'fields': ('headline_uk', 'content_uk', ),
        }),
    )

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(CentreSubpageAdmin, self).formfield_for_dbfield(
            db_field, **kwargs
        )
        db_fieldname = canonical_fieldname(db_field)

        if db_fieldname == 'headline':
            field.widget = forms.TextInput(attrs={
                'style': 'width:45%; max-width:45%;'
            })

        return field

    def get_admin_url(self, instance):
        url = None
        centre = getattr(instance, 'centre', None)

        if centre:
            url_name = 'admin:{}_{}_change'.format(
                centre._meta.app_label, centre._meta.model_name)
            url = reverse(url_name, args=[centre.id])

        return url

    def centre_preview(self, instance):
        centre_preview = instance.centre
        url = self.get_admin_url(instance)

        if url:
            centre_preview = format_html(
                '<a href="{}" class="inlinechangelink">{}</a>'.format(
                    url, instance.centre))

        return centre_preview
    centre_preview.short_description = Centre._meta.verbose_name


# Worksheet

@admin.register(Worksheet, site=admin_site)
class WorksheetAdmin(DefaultOrderingModelAdmin):
    pass
