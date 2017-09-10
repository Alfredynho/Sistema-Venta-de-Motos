from django.contrib import admin
from .models import Proveedor


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
	list_display = (
		'id','nombre','direccion','telefono',
		'ciudad','email','habilitado')

	list_search = ('nombre',)

	class Meta:
		models = Proveedor