# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 03:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_author_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exppost',
            old_name='pud_date',
            new_name='pub_date',
        ),
        migrations.AddField(
            model_name='exppost',
            name='post_type',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
