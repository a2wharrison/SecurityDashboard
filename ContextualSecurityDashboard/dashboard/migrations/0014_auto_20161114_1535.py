# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-14 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_auto_20161107_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='acknowledged',
            field=models.CharField(choices=[('', ''), ('V', 'Viewed'), ('F', 'Fixed')], max_length=1),
        ),
    ]
