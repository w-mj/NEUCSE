# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-12 02:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online', '0004_auto_20170718_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='userrank',
            field=models.IntegerField(default=0),
        ),
    ]
