# act_project/act/website/models.py
import os

from urllib.parse import urljoin

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.template.defaultfilters import filesizeformat

from transliterate import translit
from ckeditor.fields import RichTextField
from stdimage.models import StdImageField

from act.validators import FileContentTypeValidator
from act.utils import get_default_URL
# Notice overridden transmeta import!
from act.services.transmeta import TransMeta
from act.services.file_name import RandomFileName

from .validators import (
    top_event_validator,
    problem_description_validator,
    activity_description_validator,
)

"""
Hack to order models in Django Admin. Whitespaces assigned in nested Meta
classes are concatenated with verbose_name_plural to force ordering by
whitespaces number
"""
models.options.DEFAULT_NAMES += ('order_prefix',)


def get_table_name(*args):
    ''' Getting the correct and clean table name '''
    app_label = 'website'
    return '_'.join((app_label, ) + args)


class FixedStdImageField(StdImageField):
    '''
    Specified default width and height for a StdImageField that
    could be later used in consuming model attributes definition
    '''
    MAX_WIDTH = 1920
    MAX_HEIGHT = 1280


# Content

class ContentBlock(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.name) or self.__class__.__name__

    def get_template_block_name(self):
        return self.name.replace(' ', '_').lower()


class IntroContent(ContentBlock, metaclass=TransMeta):
    headline = models.CharField('Вступна фраза', max_length=200)

    class Meta:
        db_table = get_table_name('content', 'intro')

        order_prefix = ' ' * 15

        verbose_name = 'Контент - Інтро'
        verbose_name_plural = order_prefix + verbose_name

        translate = ('headline', )


class AboutContent(ContentBlock, metaclass=TransMeta):
    title = models.CharField('Заголовок', max_length=200)
    text = models.TextField('Текст', max_length=2000)

    class Meta:
        db_table = get_table_name('content', 'about')

        order_prefix = ' ' * 14

        verbose_name = 'Контент - Про нас'
        verbose_name_plural = order_prefix + verbose_name

        translate = ('title', 'text', )


class GoalContent(ContentBlock, metaclass=TransMeta):
    title = models.CharField('Заголовок', max_length=200)
    text = models.TextField('Текст', max_length=2000)

    class Meta:
        db_table = get_table_name('content', 'goal')

        order_prefix = ' ' * 13

        verbose_name = 'Контент - Мета'
        verbose_name_plural = order_prefix + verbose_name

        translate = ('title', 'text', )


# Links

class Sponsor(models.Model, metaclass=TransMeta):
    LOGO_PATH = 'sponsors/logos/'

    logo = models.ImageField('Логотип', upload_to=RandomFileName(LOGO_PATH))

    title = models.CharField('Назва організації', max_length=100)
    link = models.URLField('Посилання', max_length=300)

    class Meta:
        db_table = get_table_name('sponsors')

        order_prefix = ' ' * 12

        verbose_name = 'Донор'
        verbose_name_plural = order_prefix + 'Донори'

        translate = ('title', )

    def __str__(self):
        return str(self.title) or self.__class__.__name__

    def logo_preview(self):
        return '<img src="%s" width="100" max-width="100">' % (self.logo.url)
    logo_preview.allow_tags = True
    logo_preview.short_description = 'Логотип'


class Social(models.Model):
    title = models.CharField('Назва мережі', max_length=50)
    link = models.URLField('Посилання', max_length=300)
    icon = models.CharField('Іконка', max_length=30)

    class Meta:
        db_table = get_table_name('socials')

        order_prefix = ' ' * 11

        verbose_name = 'Соціальна мережа'
        verbose_name_plural = order_prefix + 'Соціальні мережі'

    def __str__(self):
        return str(self.title) or self.__class__.__name__


# Activity

class Activity(models.Model, metaclass=TransMeta):
    title = models.CharField('Назва діяльності', max_length=100)
    icon = models.CharField('Іконка', max_length=30)

    class Meta:
        db_table = get_table_name('activities')

        order_prefix = ' ' * 10

        verbose_name = 'Вид діяльності'
        verbose_name_plural = order_prefix + 'Види діяльності'

        translate = ('title', )

    def __str__(self):
        return str(self.title) or self.__class__.__name__


# AttachedDocument

def attached_document_upload_to(instance, filename):
    return instance.get_document_path(instance, filename)


class AttachedDocument(models.Model, metaclass=TransMeta):
    DOCUMENT_PATH = 'documents/'

    allowed_content_types = (
        'image/jpeg',
        'application/pdf',
        'application/msword',
        ('application/'
         'vnd.openxmlformats-officedocument.wordprocessingml.document'),
        ('application/'
         'vnd.openxmlformats-officedocument.wordprocessingml.document'),
        'application/vnd.ms-excel',
        'application/octet-stream',
        ('application/'
         'vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
        'application/vnd.ms-powerpoint',
        ('application/'
         'vnd.openxmlformats-officedocument.presentationml.presentation'),
    )
    allowed_content_types_extensions = (
        '.jpeg', '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx')
    max_size = 1024 * 5120

    content_type_validator = FileContentTypeValidator(
        # `max_size` of 5 megabytes
        max_size=max_size,
        allowed_content_types=allowed_content_types)

    document = models.FileField(
        'Документ',
        upload_to=attached_document_upload_to,
        validators=[content_type_validator],
        help_text=(
            "Дозволені типи файлів: " +
            ", ".join(allowed_content_types_extensions) +
            "\n"
            "Максимальний розмір файлу: " +
            filesizeformat(max_size))
    )
    description = models.CharField('Короткий опис', max_length=200)

    class Meta:
        abstract = True

        translate = ('description', )

    def __str__(self):
        return str(self.description) or self.__class__.__name__

    @staticmethod
    def get_document_path(instance, filename, path=None):
        '''
        This static method is actually a callable for `upload_to` file
        field argument, which is called after instance already created (and
        does not exist during file field definition). It's also called by
        subclasses to concatenate root document path with their subfolders
        '''
        document_path = AttachedDocument.DOCUMENT_PATH

        if path is not None:
            document_path = os.path.join(document_path, path)

        '''
        RandomFileName implements `__call()__` which expects the same
        arguments as `upload_to` callable - `instance` and `filename`
        '''
        random_file_name = RandomFileName(document_path)

        return random_file_name(instance, filename)


# Project

class ProjectArea(models.Model, metaclass=TransMeta):
    title = models.CharField('Назва', max_length=100, unique=True)

    class Meta:
        db_table = get_table_name('projects', 'areas')

        order_prefix = ' ' * 5

        verbose_name = 'Напрямок проекту'
        verbose_name_plural = order_prefix + 'Напрямки проектів'

        translate = ('title', )

    def __str__(self):
        return str(self.title) or self.__class__.__name__

    ''' Projects shortcut methods '''

    def get_projects(self):
        return self.projects.all()

    def get_projects_count(self):
        return self.projects.count()
    get_projects_count.short_description = 'Кількість проектів'


class Project(models.Model, metaclass=TransMeta):
    LIMIT = {'default': 3, 'max': 100}
    PAGE_SIZE = {'default': 4, 'max': 100}

    IMAGE_PATH = 'projects/images/'

    variations = {
        'wide': {
            'width': FixedStdImageField.MAX_WIDTH,
            'height': 810,
            'crop': True},
    }

    image = FixedStdImageField(
        'Головне зображення',
        upload_to=RandomFileName(IMAGE_PATH),
        variations=variations)

    project_area = models.ForeignKey(
        ProjectArea,
        null=True,
        on_delete=models.SET_NULL,
        related_name='projects',
    )
    project_area.verbose_name = ProjectArea._meta.verbose_name

    title = models.CharField('Назва', max_length=200, unique=True)
    started_at = models.DateField('Дата початку', auto_now_add=True)
    content = RichTextField(
        'Контент', config_name='article_toolbar',
    )
    is_active = models.BooleanField(
        'Відображається', blank=True, default=True,
    )

    # TODO: slug doesn't support i18n for now
    slug = models.SlugField(editable=False)

    class Meta:
        db_table = get_table_name('projects')

        order_prefix = ' ' * 4

        verbose_name = 'Проект'
        verbose_name_plural = order_prefix + 'Проекти'

        ordering = ('started_at', )

        translate = ('title', 'content', )

    def __str__(self):
        return str(self.title) or self.__class__.__name__

    def save(self, *args, **kwargs):
        if self.title:
            # TODO: 'uk' parameter should be changed in case of extra locale
            transliterated = translit(self.title, 'uk', reversed=True)
            self.slug = slugify(transliterated).replace('-', '_')

        super(Project, self).save(*args, **kwargs)

    def image_preview(self):
        return '<img src="%s" width="300" max-width="300">' % (self.image.url)
    image_preview.allow_tags = True
    image_preview.short_description = 'Превʼю головного зображення'

    '''Events shortcut methods'''

    def get_events(self):
        return self.events.all()

    def get_events_count(self):
        return self.events.count()
    get_events_count.short_description = 'Кількість подій'


class ProjectAttachedDocument(AttachedDocument):
    DOCUMENT_PATH = 'projects/'

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='project_attached_documents',
    )

    class Meta:
        db_table = get_table_name('projects', 'attached', 'documents')

        verbose_name_plural = "Прикріплені документи"

    def get_document_path(self, instance, filename):
        return super().get_document_path(
            instance, filename, self.DOCUMENT_PATH)


# Event

class EventCategory(models.Model, metaclass=TransMeta):
    title = models.CharField('Назва', max_length=100, unique=True)

    class Meta:
        db_table = get_table_name('events', 'categories')

        order_prefix = ' ' * 3

        verbose_name = 'Категорія події'
        verbose_name_plural = order_prefix + 'Категорії подій'

        translate = ('title', )

    def __str__(self):
        return str(self.title) or self.__class__.__name__

    '''Events shortcut methods'''

    def get_events(self):
        return self.events.all()

    def get_events_count(self):
        return self.events.count()
    get_events_count.short_description = 'Кількість подій'


class EventManager(models.Manager):
    def filter_created_at_gt(self, datetime):
        return super(EventManager, self).get_queryset().filter(
            is_active=True, created_at__gt=datetime)

    def order_by_created_at_limit(self):
        return (
            super(EventManager, self).get_queryset()
            .filter(is_active=True,)
            .order_by('-created_at')
            [:self.model.LIMIT['default']]
        )


class Event(models.Model, metaclass=TransMeta):
    LIMIT = {'default': 6, 'max': 100}
    PAGE_SIZE = {'default': 4, 'max': 100}

    IMAGE_PATH = 'events/images/'

    variations = {
        'square': {'width': 480, 'height': 480, 'crop': True},
        'wide': {
            'width': FixedStdImageField.MAX_WIDTH,
            'height': 810,
            'crop': True},
    }

    image = FixedStdImageField(
        'Головне зображення',
        upload_to=RandomFileName(IMAGE_PATH),
        variations=variations)

    event_category = models.ForeignKey(
        EventCategory,
        null=True,
        on_delete=models.SET_NULL,
        related_name='events',
    )
    event_category.verbose_name = EventCategory._meta.verbose_name

    project = models.ForeignKey(
        Project,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='events',
    )
    project.verbose_name = Project._meta.verbose_name

    created_at = models.DateTimeField('Дата та час події', auto_now_add=True)
    title = models.CharField('Назва', max_length=200)
    content = RichTextField(
        'Контент', config_name='article_toolbar',
    )
    is_active = models.BooleanField(
        'Відображається', blank=True, default=True,
    )

    slug = models.SlugField(editable=False)

    objects = EventManager()

    class Meta:
        db_table = get_table_name('events')

        order_prefix = ' ' * 2

        verbose_name = 'Подія'
        verbose_name_plural = order_prefix + 'Події'

        ordering = ('created_at', )

        translate = ('title', 'content', )

    def __str__(self):
        return str(self.title) or self.__class__.__name__

    def save(self, *args, **kwargs):
        if self.title:
            # TODO: 'uk' parameter should be changed in case of extra locale
            transliterated = translit(self.title, 'uk', reversed=True)
            self.slug = slugify(transliterated).replace('-', '_')

        super(Event, self).save(*args, **kwargs)

    def image_preview(self):
        return '<img src="%s" width="300" max-width="300">' % (self.image.url)
    image_preview.allow_tags = True
    image_preview.short_description = 'Превʼю головного зображення'

    def get_static_path(self):
        ''' Static path for front end application '''
        return 'events/{}/{}'.format(self.id, self.slug)

    def get_static_URL(self):
        '''
        Static URL for front end application,
        built with static DEFAULT_URL setting
        '''
        return urljoin(get_default_URL(), self.get_static_path())


class EventAttachedDocument(AttachedDocument):
    DOCUMENT_PATH = 'events/'

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='event_attached_documents',
    )

    class Meta:
        db_table = get_table_name('events', 'attached', 'documents')

        verbose_name_plural = "Прикріплені документи"

    def get_document_path(self, instance, filename):
        return super().get_document_path(
            instance, filename, self.DOCUMENT_PATH)


# City

class City(models.Model, metaclass=TransMeta):
    PHOTO_PATH = 'cities/photos/'

    variations = {
        'square': {'width': 480, 'height': 480, 'crop': True},
        'high': {
            'width': 400,
            'height': FixedStdImageField.MAX_HEIGHT,
            'crop': True},
    }

    photo = FixedStdImageField(
        'Фотографія',
        upload_to=RandomFileName(PHOTO_PATH),
        variations=variations)

    name = models.CharField('Назва', max_length=100, unique=True)

    class Meta:
        db_table = get_table_name('cities')

        order_prefix = ' ' * 9

        verbose_name = 'Місто'
        verbose_name_plural = order_prefix + 'Міста'

        translate = ('name', )

    def __str__(self):
        return str(self.name) or self.__class__.__name__

    def photo_preview(self):
        return '<img src="%s" width="400" max-width="400">' % (self.photo.url)
    photo_preview.allow_tags = True
    photo_preview.short_description = 'Превʼю фотографії'


# Centre

class Centre(models.Model, metaclass=TransMeta):
    city = models.OneToOneField(
        City, null=True, on_delete=models.SET_NULL
    )
    city.verbose_name = City._meta.verbose_name

    projects = models.ManyToManyField(
        Project, blank=True, related_name='centres'
    )
    projects.verbose_name = Project._meta.verbose_name_plural

    events = models.ManyToManyField(
        Event, blank=True, related_name='centres'
    )
    events.verbose_name = Event._meta.verbose_name_plural

    top_event = models.ForeignKey(
        Event,
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    top_event.verbose_name = 'Головна подія'

    short_description = models.CharField('Короткий опис', max_length=500)

    class Meta:
        db_table = get_table_name('centres')

        order_prefix = ' ' * 8

        verbose_name = 'Центр'
        verbose_name_plural = order_prefix + 'Центри'

        translate = ('short_description', )

    def __str__(self):
        return str(self.city) if self.city else self.__class__.__name__

    def clean(self, *args, **kwargs):
        '''
        Validation errors are raised in bunch, so user could
        see them all at once - not one by one on each error
        '''
        super(Centre, self).clean(*args, **kwargs)

        errors = {}

        error_top_event = top_event_validator(self.top_event, self.events)
        if error_top_event:
            errors['top_event'] = [error_top_event]

        if errors:
            raise ValidationError(errors)

    '''Projects shortcut methods'''

    def get_projects(self):
        return self.projects.all()

    def get_projects_count(self):
        return self.projects.count()
    get_projects_count.short_description = 'Кількість проектів'

    '''Events shortcut methods'''

    def get_events(self):
        return self.events.all()

    def get_events_count(self):
        return self.events.count()
    get_events_count.short_description = 'Кількість подій'

    '''Participants shortcut methods'''

    def get_participants(self):
        return self.participants.all()

    def get_participants_count(self):
        return self.participants.count()
    get_participants_count.short_description = 'Кількість співробітників'

    '''Subpages shortcut methods'''

    def get_subpages(self):
        return self.centres_subpages.all()


class CentreSubpage(models.Model, metaclass=TransMeta):
    centre = models.ForeignKey(
        Centre, on_delete=models.CASCADE, related_name='centres_subpages',
    )

    headline = models.CharField('Назва сторінки', max_length=100)
    content = RichTextField(
        'Контент', config_name='article_toolbar',
    )

    class Meta:
        db_table = get_table_name('centres', 'subpages')

        order_prefix = ' ' * 7

        verbose_name = 'Підсторінка Центру'
        verbose_name_plural = order_prefix + 'Підсторінки Центрів'

        translate = ('headline', 'content', )

    def __str__(self):
        return str(self.headline) or self.__class__.__name__


# Participant

class Participant(models.Model, metaclass=TransMeta):
    PHOTO_PATH = 'participants/photos/'

    variations = {
        'square': {'width': 480, 'height': 480, 'crop': True},
    }

    photo = FixedStdImageField(
        'Фотографія',
        upload_to=RandomFileName(PHOTO_PATH),
        variations=variations)

    centre = models.ForeignKey(
        Centre,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='participants',
    )
    centre.verbose_name = Centre._meta.verbose_name

    position = models.CharField('Посада', max_length=100)
    name = models.CharField('Імʼя', max_length=200)
    surname = models.CharField('Прізвище', max_length=200)

    class Meta:
        db_table = get_table_name('participants')

        order_prefix = ' ' * 6

        verbose_name = 'Співробітник'
        verbose_name_plural = order_prefix + 'Співробітники'

        translate = ('position', 'name', 'surname', )

    def __str__(self):
        return self.get_full_name() or self.__class__.__name__

    def photo_preview(self):
        return '<img src="%s" width="200" max-width="200">' % (self.photo.url)
    photo_preview.allow_tags = True
    photo_preview.short_description = 'Превʼю фотографії'

    def get_full_name(self):
        if not (self.name or self.surname):
            return None

        return "%s %s" % (self.name, self.surname)
    get_full_name.short_description = 'Повне імʼя'


# Contact

class Contact(models.Model, metaclass=TransMeta):
    centre = models.OneToOneField(
        Centre, null=True, blank=True, on_delete=models.CASCADE,
    )
    centre.verbose_name = Centre._meta.verbose_name

    email = models.EmailField('E-mail', max_length=254)
    phone = models.CharField('Телефон', max_length=19)
    address = models.CharField(
        'Адреса', max_length=300, null=True, blank=True,
    )

    class Meta:
        db_table = get_table_name('contacts')

        order_prefix = ' ' * 6

        verbose_name = 'Контакт'
        verbose_name_plural = order_prefix + 'Контакти'

        translate = ('address', )

    def __str__(self):
        return str(self.centre) if self.centre else self.__class__.__name__


# Worksheet

class Worksheet(models.Model):
    full_name = models.CharField('ПІБ',  max_length=300)
    residence = models.CharField('Місце проживання', max_length=500)
    email = models.EmailField('E-mail', max_length=254)
    phone = models.CharField('Телефон', max_length=19)
    personal_link = models.URLField(
        'Персональна сторінка', max_length=200, null=True, blank=True,
    )
    problem = models.NullBooleanField('Бажаєте повідомити про проблему?')
    problem_description = models.CharField(
        'Із якою проблемою Вам довелося зіштовхнутися?',
        max_length=1000,
        null=True,
        blank=True,
    )
    activity = models.NullBooleanField('Чи бажаєте Ви долучитись до «ДІЙ!»?')
    activity_description = models.CharField(
        'У якій діяльності в рамках «ДІЙ!» ви би хотіли взяти участь?',
        max_length=1000,
        null=True,
        blank=True,
    )

    class Meta:
        db_table = get_table_name('worksheet')

        order_prefix = ' ' * 1

        verbose_name = 'Анкета'
        verbose_name_plural = order_prefix + 'Анкети'

    def __str__(self):
        return str(self.full_name) or self.__class__.__name__

    def clean(self, *args, **kwargs):
        '''
        Validation errors are raised in bunch, so user could
        see them all at once - not one by one on each error
        '''
        super(Worksheet, self).clean(*args, **kwargs)

        errors = {}

        error_problem_description = problem_description_validator(
            self.problem, self.problem_description)
        if error_problem_description:
            errors['problem_description'] = [error_problem_description]

        error_activity_description = activity_description_validator(
            self.activity, self.activity_description)
        if error_activity_description:
            errors['activity_description'] = [error_activity_description]

        if errors:
            raise ValidationError(errors)
