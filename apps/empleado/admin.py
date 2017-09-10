# -*- encoding: utf-8 -*-

from django.contrib import admin
from .models import Empleado


@admin.register(Empleado)
class AdminEmpleado(admin.ModelAdmin):
	list_display = ('empleado', 'cedula','celular','tipo', 'habilitado')

	search_fields = ('cedula',)

	class Meta:
		models = Empleado