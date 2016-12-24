# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-24 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20161224_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='attached_documents',
            field=models.ManyToManyField(blank=True, related_name='events', to='website.AttachedDocument'),
        ),
    ]