# coding: utf-8
from django.db import models
from django.conf import settings
from django.db.models import signals
from django.utils.translation import ugettext_lazy as _

import decimal

from apps.producto.models import Producto
from apps.cliente.models import Cliente

class Venta(models.Model):

    cliente = models.ForeignKey(
        Cliente,
        verbose_name = _('Cliente'),
        default=None
    )

    fecha = models.DateField(
    	auto_now_add=True
    )

    total = models.FloatField(
        default = 0
    )

    iva = models.FloatField(
        default=0
      )

    vendedor = models.ForeignKey(
    	settings.AUTH_USER_MODEL
    )


    def __str__(self):
    	return '%s - %s - %s - %s - %s' % (self.id ,self.cliente, self.vendedor, self.total, self.fecha)



class DetalleVenta(models.Model):

    factura = models.ForeignKey(
    	Venta, 
    	db_column='venta_id', 
    	related_name='venta'
    )

    producto = models.ForeignKey(
    	Producto, 
    	db_column='producto_id'
    )

    precio = models.DecimalField(
    	max_digits=6, 
    	decimal_places=2
    )

    cantidad = models.IntegerField()


    subtotal = models.FloatField(
        default = 0
    )


    def nombre_sucursal(self):
    	return self.sucursal.nombre

    def marca_producto(self):
    	return self.producto.marca

    def producto_vendido(self):
    	return self.producto.numero_serie


def update_stock(sender, instance, **kwargs):
    instance.producto.cantidad -= instance.cantidad
    instance.producto.save()

signals.post_save.connect(update_stock, sender=DetalleVenta, dispatch_uid="update_stock_count")
