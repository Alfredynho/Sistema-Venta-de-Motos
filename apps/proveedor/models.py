# -*- encoding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _

class Proveedor(models.Model):

	nombre = models.CharField(
		verbose_name = _('Nombre'),
		max_length=50,
		null=True,
		blank=True
	)

	direccion = models.CharField(
		verbose_name = _('Direccion'),
		max_length=100,
		null=True,
		blank=True
	)

	telefono = models.IntegerField(
		verbose_name = _('Telefono'),
		null=True,
		blank=True
	)

	ciudad = models.CharField(
		verbose_name = _('Ciudad'),
		max_length=20,
		null=True,
		blank=True
	)

	email = models.EmailField(
		verbose_name = _('Email'),
		max_length=50,
		null=True,
		blank=True
	)

	habilitado = models.BooleanField(
		verbose_name =_('Habilitado'),
		default=True
	)
		
	class Meta:
		ordering = ['nombre']
		verbose_name_plural = "Proveedores"

	def __str__(self):
		return self.nombre 





