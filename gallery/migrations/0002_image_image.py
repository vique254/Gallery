# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-16 12:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(default=datetime.datetime(2019, 12, 16, 12, 39, 3, 863852, tzinfo=utc), upload_to='categories/'),
            preserve_default=False,
        ),
    ]
