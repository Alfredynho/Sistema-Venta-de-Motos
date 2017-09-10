# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-08 00:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre')),
                ('direccion', models.CharField(blank=True, max_length=100, null=True, verbose_name='Direccion')),
                ('telefono', models.CharField(blank=True, max_length=10, null=True, verbose_name='Telefono')),
                ('ciudad', models.CharField(blank=True, max_length=20, null=True, verbose_name='Ciudad')),
                ('email', models.EmailField(blank=True, max_length=50, null=True, verbose_name='Correo electrónico')),
                ('habilitado', models.BooleanField(default=True, verbose_name='Habilitado')),
            ],
            options={
                'verbose_name_plural': 'Proveedores',
                'ordering': ['nombre'],
            },
        ),
    ]
