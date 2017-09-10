# -*- encoding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import signals

from apps.empleado.models import Empleado
from apps.cliente.models import Cliente
from apps.repuesto.models import Repuesto
from apps.producto.models import Producto


# Estados de la reparacion del vehiculo
# La Moto esta en el taller, pero no se ha revisado
# PENDIENTE = 'Pendiente'  -> FECHA INICIO_REPARACION
# # Ya esta la esta en el taller
# RECIBIDO = 'Recibido' -> FECHA INICIO_REPARACION
# # La moto ya esta reparada
# REPARADO = 'Reparado' -> FECHA FIN_REPARACION
# # La motocicleta fue reparada y entregada al cliente
# REPARADO_Y_ENTREGADO = 'Reparado y entregado' -> FECHA FIN_REPARACION
# # La motocicleta fue retirada ya que el cliente no acepto su reparacion
# RETIRADO = 'Retirado' -> FECHA FIN REPARACION


ESTADO = (
	("PENDIENTE", 'Pendiente'),
	("RECIBIDO", 'Recibido'),
	("REPARADO", 'Reparado'),
	("REPARADO_Y_ENTREGADO", 'Reparado y entregado'),
	("RETIRADO", 'Retirado'),
 )


class Asistencia(models.Model):

	empleado = models.ForeignKey(
		Empleado,
		default = None,
		verbose_name = _('Empleado')
	)

	cliente = models.ForeignKey(
		Cliente,
		default = None,
		verbose_name = _('Cliente')
	)

	motocicleta = models.ForeignKey(
		Producto,
		default = None,
		verbose_name = _('Motocicleta')
	)

	placa = models.CharField(
		null =True,
		blank = True,
		max_length = 20,
		verbose_name = _('Placa')
	)

	fecha_entrada = models.DateField(
		auto_now_add=True,
		blank=True, 
		null=True,
		verbose_name = _('Fecha Entrada')
	)

	fecha_salida = models.DateField(
		blank=True, 
		null=True,
		verbose_name = _('Fecha Salida')
	)

	estado_reparacion = models.CharField(
		max_length = 30,
		choices = ESTADO,
		default = "PENDIENTE",
		verbose_name = _('Estado Reparacion')
	)

	observacion = models.TextField(
		null=True,
		blank=True,
		max_length=200,
		verbose_name = _('Observacion')
	)

	total = models.DecimalField(
		max_digits=8, 
		decimal_places=2, 
		null=True, 
		blank=True
	)

	habilitado = models.BooleanField(
		default = True,
		verbose_name = _('Habilitado')
	)


	def nombre(self):
		return self.empleado.empleado.first_name 

	class Meta:
		ordering = ['fecha_entrada']
		verbose_name_plural = "Asistencia de Motocicleta"
		unique_together = ('placa','fecha_salida')


	def __str__(self):
		return self.motocicleta.marca


class DetalleAsistencia(models.Model):

	reparacion = models.ForeignKey(
		Asistencia,
		db_column = 'asistencia_id',
		related_name = 'asistencia'	
	)

	repuesto = models.ForeignKey(
		Repuesto,
		db_column = 'repuesto_id'
	)

	cantidad = models.IntegerField()

	descripcion = models.TextField(
		help_text = 'Descripcion de por que se esta agregando el repuesto',
		verbose_name = _('Descripcion')
	)

	fecha = models.DateField()

	estado = models.BooleanField(
		default = True,
		verbose_name = _('Estado')
	)


	def marca_producto(self):
		return self.producto.marca

def update_stock(sender, instance, **kwargs):
	instance.repuesto.cantidad -= instance.cantidad
	instance.repuesto.save()

signals.post_save.connect(update_stock, sender=DetalleAsistencia, dispatch_uid="update_stock_count")
