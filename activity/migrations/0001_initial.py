# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-21 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.CharField(max_length=1024, verbose_name='活动对象')),
                ('created_at', models.DateTimeField(verbose_name='创建时间')),
                ('type', models.IntegerField(choices=[(1, '发布了文章'), (2, '发布了照片'), (3, '添加了评论'), (4, '闲扯了几句')],
                                             verbose_name='活动种类')),
            ],
        ),
    ]
