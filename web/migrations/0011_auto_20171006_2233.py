# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-06 22:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_auto_20171004_2314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='housingresources',
            name='deposit',
        ),
        migrations.AddField(
            model_name='housingresources',
            name='bet',
            field=models.IntegerField(default=0, verbose_name='\u62bc'),
        ),
        migrations.AddField(
            model_name='housingresources',
            name='pay',
            field=models.IntegerField(default=0, verbose_name='\u4ed8'),
        ),
    ]
