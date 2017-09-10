from django.conf.urls import url
from .views import buscarCliente, buscarProducto,ventaCrear, ListaVentas,reporteventas

urlpatterns = (

    url(r'venta/lista_ventas/$', ListaVentas.as_view(), name = 'lista_ventas'),
    url(r'^venta/buscar_cliente/$', buscarCliente, name = "buscar_cliente"),
    url(r'^venta/buscar_producto/$', buscarProducto , name = "buscar_producto"),
   	url(r'^venta/productos/$', ventaCrear, name="venta_productos"),
    url(r'^factura/detalle/(?P<pk>\d+)/$', reporteventas , name="factura_venta_detalle"),
    
    # url(r'^factura/consultar$', 'apps.factura.views.consultarFactura', name="consultar_factura"),

    # url (r'factura/generar_reporte_factura/$', generar_pdf, name = 'generar_reporte_factura'),

    # url(r'factura/reporte_ventas/(?P<pk>\d+)/$', 'apps.factura.views.reporteventas', name='reporte_ventas'),

   )
