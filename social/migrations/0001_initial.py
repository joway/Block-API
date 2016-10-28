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
            name='SocialAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(blank=True, max_length=255, null=True, verbose_name='uid')),
                ('username', models.CharField(blank=True, max_length=32, verbose_name='用户名')),
                ('expire_at', models.DateTimeField(blank=True, null=True, verbose_name='token失效时间')),
                ('access_token', models.CharField(blank=True, max_length=255, null=True, verbose_name='access_token')),
                (
                'refresh_token', models.CharField(blank=True, max_length=255, null=True, verbose_name='refresh_token')),
                ('provider',
                 models.CharField(choices=[('github', 'Github'), ('qq', 'QQ'), ('coding', 'Coding')], max_length=10,
                                  verbose_name='类别')),
            ],
        ),
    ]
