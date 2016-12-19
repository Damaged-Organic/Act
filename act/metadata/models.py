# act_project/act/metadata/models.py
from django.db import models

# Notice overridden transmeta import!
from act.services.transmeta import TransMeta


class Metadata(models.Model, metaclass=TransMeta):
    url_name = models.CharField('Роутінг', max_length=100)
    title = models.CharField('Назва сторінки', max_length=100)
    description = models.CharField('Опис сторінки', max_length=250)
    robots = models.CharField('Інформація для ботів', max_length=100)

    class Meta:
        verbose_name = 'Метадані'
        verbose_name_plural = 'Метадані'

        translate = ('title', 'description',)

    def __str__(self):
        return str(self.title) or self.__class__.__name__
