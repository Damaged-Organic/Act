# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-24 11:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20161224_1315'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attacheddocument',
            options={'verbose_name': 'Документ', 'verbose_name_plural': 'Документи'},
        ),
        migrations.AlterModelTable(
            name='attacheddocument',
            table='website_attached_documents',
        ),
    ]
