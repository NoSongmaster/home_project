# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 16:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_userinfo'),
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
            name='Firm',
        ),
        migrations.DeleteModel(
            name='Host',
        ),
        migrations.DeleteModel(
            name='Userinfo',
        ),
    ]
