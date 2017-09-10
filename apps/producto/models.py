# -*- encoding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from apps.proveedor.models import Proveedor

from .validators import validador_numero_serie

#Creacion del Choices para 'tipo' de Motocicletas

SCOOTER = 'Scooter' # Motocicletas Pequenias
URBANA = 'Urbana' # Tipo estandar
TRABAJO = 'Trabajo' # Motocicleta para trabajo
TOURING = 'Touring' # Motos para viejes, mas equipadas
CRUCERO = 'Crucero' # Motos Identificadas por su reveldia
CROSS = 'Cross' # Motos para carreras
ATV = 'atv' # Todo Terreno / Cuatrimotos
DEPORTIVA = 'Deportiva' # Motos tipo Ninja
NAKED = 'Naked' # Motos que traen algunas cosas Afuera
ACCESORIO = 'Accesorio' # Accesorio para la motocicleta

TIPO_CHOICES = (

	(SCOOTER, 'Scooter'),
	(URBANA, 'Urbana'),
	(TRABAJO, 'Trabajo'),
	(TOURING, 'Touring'),
	(CRUCERO, 'Crucero'),
	(CROSS, 'Cross'),
	(ATV, 'Atv'),
	(DEPORTIVA, 'Deportiva'),
	(NAKED, 'Naked'),
	(ACCESORIO, 'Accesorio'),

)

class Producto(models.Model):

	numero_serie = models.CharField(
		verbose_name = _('Numero Serie'),
		validators = [validador_numero_serie],
		help_text = 'Ingresa el numero de serie ej. USM-1001',
		unique = True,
		max_length = 100
	)

	nombre = models.CharField(
		verbose_name = _('Nombre'),
		max_length = 100
	)

	marca = models.CharField(
		verbose_name = _('Marca'),
		max_length = 100,
		default = 'USM'
	)

	color = models.CharField(
		verbose_name = _('Color'),
		max_length=20
	)

	cantidad = models.IntegerField(
		verbose_name= _('Cantidad')
	)

	precio_compra = models.DecimalField(
		verbose_name = _('Precio Compra'),
		max_digits = 7, 
		decimal_places = 2, 
		default = 0.00
	)

	precio_venta = models.DecimalField(
		verbose_name = _('Precio Venta'),
		max_digits = 7, 
		decimal_places = 2, 
		default = 0.00
	)

	proveedor = models.ForeignKey(
		Proveedor,
		verbose_name = _('Proveedor')
	)

	caracteristicas = models.TextField(
		verbose_name = _('Caracteristicas'),
		null = True, 
		blank = True
	)


	tipo = models.CharField(
		verbose_name = _('Tipo'),
		max_length = 50, 
		choices = TIPO_CHOICES, 
		default = SCOOTER
	)

	imagen = models.ImageField(
		verbose_name = _('Imagen'),
		null = True,
		blank = True,
		upload_to = "imagenes/productos/"
	)

	thumbnail = ImageSpecField(
		source = 'imagen',
		processors = [ResizeToFill(100, 50)],
		format = 'JPEG',
		options = {'quality': 60}
	)

	habilitado = models.BooleanField(
		verbose_name = _('Habilitado'),
		default = True
	)
	
	
	def __str__(self):
		return self.numero_serie + " " + self.tipo

	class Meta:
		ordering = ['numero_serie']
		verbose_name= 'Producto'
		verbose_name_plural = "Productos"
		

	

	
