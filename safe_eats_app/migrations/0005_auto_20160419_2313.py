# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-19 23:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safe_eats_app', '0004_auto_20160414_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspectionresult',
            name='inspection_score',
            field=models.IntegerField(),
        ),
    ]