# -*- encoding: utf-8 -*-

from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class Cliente_Admin(admin.ModelAdmin):
	list_display = ('cedula', 'nombre', 'apellidos', 'celular', 'email')
	search_fields = ('cedula', 'nombre')
