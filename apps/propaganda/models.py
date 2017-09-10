from django.db import models

from django.utils.translation import ugettext_lazy as _


class Propaganda(models.Model):
	
	nombre = models.CharField(
		max_length = 120,
		verbose_name = _('Nombre')
	)

	descripcion = models.TextField(
		verbose_name = _('Descripcion')
	)

	url = models.URLField(
		verbose_name = _('URL Propaganda'),
		max_length = 500
	)

	habilitado = models.BooleanField(
		default = True,
		verbose_name = _('Habilitado')
	)

	def __str__(self):
		return self.nombre


	class Meta:
		verbose_name = _('Propaganda')
		verbose_name_plural = _('Propagandas')