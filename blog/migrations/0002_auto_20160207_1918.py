# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-07 21:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 7, 21, 18, 44, 803000, tzinfo=utc)),
        ),
    ]
