# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-09 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='total',
            field=models.FloatField(default=0),
        ),
    ]
