# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from .views import (
	ListaClientes, 
	DetalleView,
	ActualizarView,
	CreateClientes,
	EliminarView,
	generar_reporte_clientes
	)

urlpatterns = [

	url(r'^clientes/$', ListaClientes.as_view(), name = 'lista_clientes'),
	url(r'^clientes/detalle/(?P<pk>\d+)/$', DetalleView.as_view(),name='detalle_cliente'),
	url(r'^clientes/actualizar/(?P<pk>\d+)/$', ActualizarView.as_view(), name ="actualizar_cliente"),
	url(r'^clientes/agregar$', CreateClientes.as_view(), name='crear_cliente'),
	url(r'^clientes/eliminar/(?P<pk>\d+)/$', EliminarView.as_view(), name="eliminar_cliente"), 
	url(r'^clientes/reporte/$', generar_reporte_clientes,name='reporte'),
	]
