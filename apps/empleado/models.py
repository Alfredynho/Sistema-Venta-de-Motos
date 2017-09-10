# -*- encoding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
		

VENDEDOR = 'Vendedor'
MECANICO = 'Mecanico'
GERENTE = 'Gerente'

tipo_choice = (
	(VENDEDOR, 'Vendedor'),
	(MECANICO, 'Mecanico'),
	(GERENTE, 'Gerente'),
 )

class Empleado(models.Model):
	
	empleado = models.OneToOneField(
        'users.User',
		verbose_name =('Usuario'),
		related_name='empleado',
	)

	cedula = models.CharField(
		verbose_name =_('cedula'),
		max_length=20,
		unique=True,
	)


	celular = models.CharField(
		verbose_name =_('Celular'),
		max_length=20
	)

	tipo = models.CharField(
		verbose_name=_('Tipo'),
		max_length=20, 
		choices=tipo_choice,
		default=VENDEDOR
	)

	habilitado = models.BooleanField(
		verbose_name =_('Habilitado'),
		default = True
	)

	imagen = models.ImageField(
		verbose_name =_('Imagen'),
		null=True,
		blank=True,
		upload_to = "imagenes/empleado"
	)

	thumbnail = ImageSpecField(
		source='imagen',
		processors=[ResizeToFill(100, 50)],
		format='JPEG',
		options={'quality': 60}
	)

	class Meta:
		ordering = ['cedula']
		verbose_name_plural = "Empleados"

	def __str__(self):
		return '%s -  %s' % (self.empleado.first_name, self.tipo)
