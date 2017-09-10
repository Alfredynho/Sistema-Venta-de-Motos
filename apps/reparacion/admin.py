# -*- encoding: utf-8 -*-

from django.contrib import admin
from .models import Asistencia, DetalleAsistencia

class DetalleAsistenciaInline(admin.TabularInline):
	model = DetalleAsistencia

class AdminOrdenDeTrabajo(admin.ModelAdmin):
	list_display = ('id', 'empleado', 'cliente','motocicleta',
		 'placa', 'fecha_entrada', 'fecha_salida','estado_reparacion',
		 'observacion','habilitado')

	inlines = (DetalleAsistenciaInline,)

	search_fields = ('id', 'placa')


admin.site.register(Asistencia, AdminOrdenDeTrabajo)
