# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-10 09:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20170210_1052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='photo_fullscreen',
            new_name='photo',
        ),
    ]
