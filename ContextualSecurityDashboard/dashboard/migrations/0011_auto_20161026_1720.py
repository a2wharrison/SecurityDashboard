# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-26 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_auto_20161024_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='severity',
            field=models.IntegerField(blank=True),
        ),
    ]
