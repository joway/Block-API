# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-21 15:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='token持有者'),
        ),
        migrations.AddField(
            model_name='grant',
            name='application',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oauth.Application'),
        ),
        migrations.AddField(
            model_name='grant',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='授权用户'),
        ),
        migrations.AddField(
            model_name='application',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='应用管理员'),
        ),
    ]