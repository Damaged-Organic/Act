# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-20 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0003_auto_20161219_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-mail'),
        ),
    ]