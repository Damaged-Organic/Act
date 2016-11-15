# diy_project/diy/website/models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

from transmeta import TransMeta
from transliterate import translit

"""
Hack to order models in Django Admin. Whitespaces assigned in nested Meta
classes are concatenated with verbose_name_plural to force ordering by
whitespaces number
"""
models.options.DEFAULT_NAMES += ('order_prefix',)


def get_table_name(*args):
    """ Getting the correct and clean table name """
    app_label = 'website'
    return '_'.join((app_label, ) + args)


# Content

class ContentBlock(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name or self.__name__

    def get_template_block_name(self):
        return self.name.replace(' ', '_').lower()


class IntroContent(ContentBlock, metaclass=TransMeta):
    headline = models.CharField('Слоган', max_length=50)

    class Meta:
        db_table = get_table_name('content', 'intro')

        order_prefix = ' ' * 100

        verbose_name = 'Блок "Інтро"'
        verbose_name_plural = order_prefix + verbose_name

        translate = ('headline',)


# Common

class Centre(models.Model, metaclass=Transmeta):
    pass


class City(models.Model, metaclass=Transmeta):
    pass


class Project(models.Model, metaclass=Transmeta):
    pass


class ProjectArea(models.Model, metaclass=Transmeta):
    pass


class ProjectInfo(models.Model, metaclass=Transmeta):
    pass


class Event(models.Model, metaclass=Transmeta):
    pass


class EventCategory(models.Model, metaclass=Transmeta):
    pass


class Participant(models.Model, metaclass=Transmeta):
    pass


class Contact(models.Model, metaclass=Transmeta):
    pass
