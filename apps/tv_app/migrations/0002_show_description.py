# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-16 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
