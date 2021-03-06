# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 23:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('repuesto', '0001_initial'),
        ('producto', '0004_remove_producto_iva'),
        ('empleado', '0001_initial'),
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(blank=True, max_length=20, null=True, verbose_name='Placa')),
                ('fecha_entrada', models.DateField(auto_now_add=True, null=True, verbose_name='Fecha Entrada')),
                ('fecha_salida', models.DateField(blank=True, null=True, verbose_name='Fecha Salida')),
                ('estado_reparacion', models.CharField(choices=[('PENDIENTE', 'Pendiente'), ('RECIBIDO', 'Recibido'), ('REPARADO', 'Reparado'), ('REPARADO_Y_ENTREGADO', 'Reparado y entregado'), ('RETIRADO', 'Retirado')], default='PENDIENTE', max_length=30, verbose_name='Estado Reparacion')),
                ('observacion', models.TextField(blank=True, max_length=200, null=True, verbose_name='Observacion')),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('habilitado', models.BooleanField(default=True, verbose_name='Habilitado')),
                ('cliente', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente', verbose_name='Cliente')),
                ('empleado', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='empleado.Empleado', verbose_name='Empleado')),
                ('motocicleta', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='producto.Producto', verbose_name='Motocicleta')),
            ],
            options={
                'ordering': ['fecha_entrada'],
                'verbose_name_plural': 'Asistencia de Motocicleta',
            },
        ),
        migrations.CreateModel(
            name='DetalleAsistencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('descripcion', models.TextField(help_text='Descripcion de por que se esta agregando el repuesto', verbose_name='Descripcion')),
                ('fecha', models.DateField()),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('reparacion', models.ForeignKey(db_column='asistencia_id', on_delete=django.db.models.deletion.CASCADE, related_name='asistencia', to='reparacion.Asistencia')),
                ('repuesto', models.ForeignKey(db_column='repuesto_id', on_delete=django.db.models.deletion.CASCADE, to='repuesto.Repuesto')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='asistencia',
            unique_together=set([('placa', 'fecha_salida')]),
        ),
    ]
