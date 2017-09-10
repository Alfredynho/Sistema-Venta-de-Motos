from django.contrib import admin

from .models import Repuesto

@admin.register(Repuesto)
class RepuestoAdmin(admin.ModelAdmin):
	list_display = ('numero_serie','nombre', 'marca', 'color','cantidad','precio_compra', 'precio_venta', 'caracteristicas', 'proveedor','habilitado')
	search_fields = ('numero_serie','nombre')