# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-19 16:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
    ]
