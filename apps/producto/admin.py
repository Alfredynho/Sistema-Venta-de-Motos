# -*- encoding: utf-8 -*-

from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):

	list_display = (
		'numero_serie', 'nombre','marca', 'precio_compra', 'precio_venta','color', 'cantidad',
		'caracteristicas', 'imagen', 'tipo', 'habilitado')

	class Meta:
		model = Producto