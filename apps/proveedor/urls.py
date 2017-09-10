# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from .views import (
	ListaProveedores, 
	DetalleView,
	ActualizarView,
	CreateProveedores,
	EliminarView,
	generar_reporte_proveedores
	)

urlpatterns = [

	url(r'^proveedores/$', ListaProveedores.as_view(), name = 'lista_proveedores'),
	url(r'^proveedores/detalle/(?P<pk>\d+)/$', DetalleView.as_view(),name='detalle_proveedor'),
	url(r'^proveedores/actualizar/(?P<pk>\d+)/$', ActualizarView.as_view(), name ="actualizar_proveedor"),
	url(r'^proveedores/agregar$', CreateProveedores.as_view(), name='crear_proveedor'),
	url(r'^proveedores/eliminar/(?P<pk>\d+)/$', EliminarView.as_view(), name="eliminar_proveedor"), 
	url(r'^proveedores/reporte/$', generar_reporte_proveedores,name='reporte'),
	]
