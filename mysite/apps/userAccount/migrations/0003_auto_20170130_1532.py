# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 06:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAccount', '0002_auto_20170130_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='nick_name',
            field=models.CharField(default=True, max_length=15, unique=True),
        ),
    ]
