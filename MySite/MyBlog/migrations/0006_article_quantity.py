# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-17 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyBlog', '0005_auto_20180611_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
