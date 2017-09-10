from django.contrib import admin

from .models import Propaganda

@admin.register(Propaganda)

class PropagandaAdmin(admin.ModelAdmin):
	list_display = ['nombre' , 'descripcion', 'url', 'habilitado']
	search_fields = ('nombre',)