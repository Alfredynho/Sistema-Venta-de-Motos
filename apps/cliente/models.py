# -*- encoding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Cliente(models.Model):

	cedula = models.CharField(
		verbose_name = _('cedula'),
		unique = True,
		max_length = 100
	)

	nombre = models.CharField(
		verbose_name = _('Nombre'),
		max_length = 100
	)

	apellidos = models.CharField(
		verbose_name = _('Apellido'),
		max_length = 100
	)


	celular = models.IntegerField(
		verbose_name = _('Celular'),
		default=0
	)

	email = models.EmailField(
		verbose_name=_('Email'), 
		max_length = 100,
		blank = True,
		null = True
	)
	
	habilitado = models.BooleanField(
		verbose_name =_('Habilitado'),
		default = True
	)

	class Meta:
		ordering = ['apellidos']
		verbose_name_plural = "Clientes"

	def __str__(self):
		return self.nombre + " " + self.apellidos