# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-21 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_post',
            field=models.BooleanField(default=True, verbose_name='是否是博文'),
        ),
    ]
