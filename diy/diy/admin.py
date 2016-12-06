# diy_project/diy/diy/admin.py
from django import forms
from django.http import HttpResponseForbidden
from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.utils.translation import ugettext as _


# Common admin mixins

class ForbidAddMixin():
    def has_add_permission(self, request):
        return False


class ForbidChangeMixin():
    '''
    Custom template to supress change functionality
    '''
    template = "admin/change_form.html"

    def change_view(self, request, object_id, form_url='', extra_context=None):
        obj = Group.objects.get(pk=object_id)

        # Set variable that contorls editable behavior
        not_editable = True

        if request.method == 'POST':
            return HttpResponseForbidden("Cannot change an inactive Group")

        more_context = {'not_editable': not_editable}
        more_context.update(extra_context or {})

        return super().change_view(request, object_id, form_url, more_context)


class ForbidDeleteMixin():
    def get_actions(self, request):
        actions = super(ForbidDeleteMixin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False


class ContentBlockMixin(ForbidDeleteMixin, ForbidAddMixin):
    exclude = ('name',)


# Admin site

class DefaultOrderingModelAdmin(admin.ModelAdmin):
    ordering = ('id',)


class DiyAdminSite(admin.AdminSite):
    site_title = 'ДІЙ!'
    site_header = 'ДІЙ!'
    index_title = 'ДІЙ! - Керування контентом'

admin_site = DiyAdminSite(name='deus_ex_machina')


@admin.register(Group, site=admin_site)
class GroupAdmin(
    ForbidAddMixin, ForbidChangeMixin, ForbidDeleteMixin, GroupAdmin
):
    readonly_fields = ('name', 'custom_permissions', )
    fields = ('name', 'custom_permissions', )

    def custom_permissions(self, obj):
        '''
        Custom field to properly format read only permissions
        '''
        return '\n'.join([
            # Careful - splitted list unpacking used here!
            '{1} : {2}'.format(*str(permission).split('|'))
            for permission in obj.permissions.all()
        ])
    custom_permissions.short_description = 'Дозволи'


@admin.register(User, site=admin_site)
class UserAdmin(UserAdmin):
    readonly_fields = ('last_login', 'date_joined', )
    list_display = (
        'custom_group',
        'username', 'email', 'first_name', 'last_name', 'is_active',
    )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Група'), {'fields': ('groups',)}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', )}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'groups', )
        }),
    )

    def custom_group(self, obj):
        '''
        Stringify groups for list view
        '''
        return ', '.join([
            group.name for group in obj.groups.all()
        ]) if obj.groups.count() else 'Суперадміністратор'
    custom_group.short_description = 'Групи'

    def get_fieldsets(self, request, obj=None):
        '''
        Set custom fieldsets for superuser
        '''
        if obj is not None and obj.is_superuser:
            fieldsets = (
                (None, {'fields': ('username', )}),
                (_('Personal info'), {
                    'fields': ('first_name', 'last_name', 'email')
                }),
            )
        else:
            fieldsets = super(UserAdmin, self).get_fieldsets(
                request, obj
            )

        return fieldsets

    def get_readonly_fields(self, request, obj=None):
        '''
        Set custom readonly fields for superuser
        '''
        if obj is not None and obj.is_superuser:
            readonly_fields = (
                'username', 'password',
            )
        else:
            readonly_fields = super(UserAdmin, self).get_readonly_fields(
                request, obj
            )

        return readonly_fields

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(UserAdmin, self).formfield_for_dbfield(
            db_field, **kwargs
        )

        if db_field.name == 'groups':
            field.widget = forms.SelectMultiple()

        return field

    def save_model(self, request, obj, form, change):
        '''
        Set default user permissions
        '''
        obj.is_staff = True
        obj.save()
