# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-23 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point_x', models.IntegerField()),
                ('point_y', models.IntegerField()),
            ],
        ),
    ]
