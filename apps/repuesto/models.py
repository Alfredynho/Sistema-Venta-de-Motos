from django.db import models

from django.utils.translation import ugettext_lazy as _
from apps.proveedor.models import Proveedor

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Repuesto(models.Model):

	numero_serie = models.CharField(
		max_length = 120,
		unique = True,
		verbose_name = _('Numero Serie')
	)

	nombre = models.CharField(
		max_length = 200,
		verbose_name = _('Nombre Repuesto')
	)

	marca = models.CharField(
		max_length = 50,
		default = 'USM',
		verbose_name = _('Marca')
	)

	precio_compra = models.DecimalField(
		max_digits = 7,
		decimal_places = 2,
		default = 0.00,
		verbose_name = _('Precio Compra')
	)


	precio_venta = models.DecimalField(
		max_digits = 7,
		decimal_places = 2,
		default = 0.00,
		verbose_name = _('Precio Venta')
	)

	color = models.CharField(
		verbose_name = _('Color'),
		null=True,
		blank=True,
		max_length=20
	)

	cantidad = models.IntegerField(
		verbose_name= _('Cantidad'),
		null=True,
		blank=True
	)
	
	caracteristicas = models.TextField(
		verbose_name = _('Caracteristicas')
	)

	proveedor = models.ForeignKey(
		Proveedor,
		verbose_name = _('Proveedor')
	)

	imagen = models.ImageField(
		verbose_name=_('Imagen'),
		null=True,
		blank=True,
		upload_to = "imagenes/repuesto/"
	)

	thumbnail = ImageSpecField(source='imagen',
									  processors=[ResizeToFill(100, 50)],
									  format='JPEG',
									  options={'quality': 60})


	habilitado = models.BooleanField(
		verbose_name=_('Habilitado'),
		default = True
	)
	

	def __str__(self):
		return self.nombre + " " + self.numero_serie
