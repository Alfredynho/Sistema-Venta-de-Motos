# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from .views import (
	ListaEmpleados, 
	DetalleView,
	ActualizarView,
	CreateEmpleados,
	EliminarView,
	generar_reporte_empleados
	)

urlpatterns = [

	url(r'^empleados/$', ListaEmpleados.as_view(), name = 'lista_empleados'),
	url(r'^empleados/detalle/(?P<pk>\d+)/$', DetalleView.as_view(),name='detalle_empleado'),
	url(r'^empleados/actualizar/(?P<pk>\d+)/$', ActualizarView.as_view(), name ="actualizar_empleado"),
	url(r'^empleados/agregar$', CreateEmpleados.as_view(), name='crear_empleado'),
	url(r'^empleados/eliminar/(?P<pk>\d+)/$', EliminarView.as_view(), name="eliminar_empleado"), 
	url(r'^empleados/reporte/$', generar_reporte_empleados,name='reporte'),
	]
