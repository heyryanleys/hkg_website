# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_auto_20170419_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='text',
            field=models.TextField(null=True),
        ),
    ]
