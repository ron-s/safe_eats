# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-13 22:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safe_eats_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantinfo',
            name='business_closed',
            field=models.BooleanField(default=False),
        ),
    ]
