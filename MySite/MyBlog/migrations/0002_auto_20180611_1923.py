# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-11 11:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyBlog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Aticle',
        ),
        migrations.AlterModelTable(
            name='aticle',
            table='aticle',
        ),
        migrations.AlterModelTable(
            name='category',
            table='category',
        ),
        migrations.AlterModelTable(
            name='tag',
            table='tag',
        ),
    ]