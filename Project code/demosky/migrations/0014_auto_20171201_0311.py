# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-01 03:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demosky', '0013_auto_20171201_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='topic',
            field=models.CharField(default='', max_length=100),
        ),
    ]
