# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 21:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_auto_20170418_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exppost',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='date work ended'),
        ),
    ]
