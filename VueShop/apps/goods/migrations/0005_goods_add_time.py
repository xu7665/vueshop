# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-17 22:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_hotsearchwords_indexad'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间'),
        ),
    ]