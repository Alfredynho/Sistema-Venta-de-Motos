from django.contrib import admin

from apps.messenger.models import  MessengerInfo

@admin.register(MessengerInfo)
class MessengerInfo(admin.ModelAdmin):
	list_display = ['messenger_id','nombre', 'apellido', 'foto_perfil', 'lugar', 'zona_horaria', 'genero']

	class Meta:
		models = MessengerInfo

