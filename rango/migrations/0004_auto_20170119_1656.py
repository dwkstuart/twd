# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-19 16:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_auto_20170119_1655'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='views2',
            new_name='views',
        ),
    ]
