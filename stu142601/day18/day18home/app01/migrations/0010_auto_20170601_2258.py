# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 14:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0009_auto_20170601_2256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host',
            name='firm',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='m',
        ),
        migrations.DeleteModel(
            name='Host',
        ),
    ]