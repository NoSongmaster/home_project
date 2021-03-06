# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 15:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0012_auto_20170601_2301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=32, unique=True)),
                ('port', models.IntegerField()),
                ('firm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Firm')),
            ],
        ),
    ]
