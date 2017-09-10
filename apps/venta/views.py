# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response as render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy, reverse
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.utils import timezone
from django.shortcuts import render

from django.db import transaction, connection
from django.contrib import messages
from django.views.generic import ListView, TemplateView, CreateView, DetailView
from django.template import RequestContext as ctx
from django.core import serializers
from django.http import HttpResponseRedirect
from django import http
from django.template.loader import get_template
from django.template import Context

import json


from apps.cliente.models import Cliente
from apps.producto.models import Producto
from apps.empleado.models import Empleado

from .models import Venta, DetalleVenta

#reporte pdf
from datetime import *
import datetime
import time

class DetalleVentaView(ListView):
    model = Venta
    context_object_name = "venta_usuario"
    template_name = 'factura/detalle_venta.html'

    def get_queryset(self):
        _idventa = self.kwargs['pk']
        venta = Venta.objects.get(id=_idventa)
        
        venta_usuario = Venta.objects.filter(id=str(venta))
        return venta_usuario

    def get_context_data(self, **kwargs):
        context = super(DetalleVentaView,self).get_context_data(**kwargs)
        context['detalle_venta'] = DetalleVenta.objects.all()
        context['venta'] = Venta.objects.all()
        return context



# funcion para crear venta
def ventaCrear(request):
    form = None
    if request.method == 'POST':
        sid = transaction.savepoint()
        try:
            proceso = json.loads(request.POST.get('proceso'))
            print("El proceso ",proceso)

            if 'clienProv' not in proceso:
                msg = 'El cliente no ha sido seleccionado'
                raise Exception(msg)

            if len(proceso['producto']) <= 0:
                msg = 'No se ha seleccionado ningun producto'
                raise Exception(msg)

            total = 0

            for k in proceso['producto']:
                producto = Producto.objects.get(id=k['serial'])
                subTotal = (producto.precio_venta) * int(k['cantidad'])
                total += subTotal
                total = total * 13

            crearFactura = Venta(
                cliente=Cliente.objects.get(id=proceso['clienProv']),
                fecha=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                total=total,
                iva = subTotal,
                vendedor=request.user
            )
            crearFactura.save()
            print("Factura guardado")
            print(crearFactura.id)
            for k in proceso['producto']:
                producto = Producto.objects.get(id=k['serial'])
                crearDetalle = DetalleVenta(
                    producto=producto,
                    precio = producto.precio_venta,
                    cantidad=int(k['cantidad']),
                    subtotal=producto.precio_venta * int(k['cantidad']),
                    factura = crearFactura,
                    )
                crearDetalle.save()

            messages.success(
                request, 'La venta se ha realizado satisfactoriamente')
        except Exception as e:
            try:
                transaction.savepoint_rollback(sid)
            except:
                pass
            messages.error(request, e)

    context = {'form':form}
    
    print("EL FORMULARIO", form)

    return render(
        request,
        'factura/crear_factura.html',
        context,
        )

        
# Funcion para Buscar Cliente
def buscarCliente(request):
    idCliente = request.GET['id']
    cliente = Cliente.objects.filter(cedula__contains=idCliente)
    data = serializers.serialize(
        'json', cliente, fields=('cedula', 'nombre', 'apellidos', 'celular'))
    return HttpResponse(data, content_type='application/json')

# Funcion para Buscar Producto
def buscarProducto(request):
    idProducto = request.GET['id']
    producto = Producto.objects.filter(numero_serie__contains=idProducto)

    print("EL PRODUCTO ", producto)
    for x in producto:
        print("\n", "PRODUCTO >>> ","\n" ,x.nombre, x.numero_serie ,"\n" , x.color,"\n",  x.tipo , "\n", x.cantidad, "\n" , x.proveedor, "\n", x.precio_venta)

    data = serializers.serialize(
        'json', producto, fields=('color','producto', 'nombre', 'iva','cantidad', 'habilitado', 'precio_venta', 'tipo'))
    print("EL DATA >>>  ", "\n" , data)

    return HttpResponse(data, content_type='application/json')

# Funcion para consulta de producto
def consultarFactura(request):
    factura = None
    detalles = None
    sum_subtotal = 0
    sum_tax = 0
    if request.method == 'POST':
        serie = request.POST.get('serie')
        numero = request.POST.get('num')

        factura = Factura.objects.get(serie=serie, numero=numero)
        detalles = DetalleFactura.objects.filter(factura=factura)

        for d in detalles:

            sum_tax = sum_tax + d.impuesto
        sum_subtotal = factura.total-sum_tax

    return render_to_response('factura/imprimir_factura.html',
                              {'factura': factura, 'detalles': detalles,
                                  'sum_subtotal': sum_subtotal, 'sum_tax': sum_tax},
                              context_instance=RequestContext(request))


class ListaVentas(ListView):
    template_name = 'factura/lista_venta.html'
    model = Venta
    
    def get_context_data(self, **kwargs):
        context = super(ListaVentas, self).get_context_data(**kwargs)
        context['Ventas'] = Venta.objects.all()
        return context


def write_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return http.HttpResponse(result.getvalue(), \
            content_type='application/pdf')
    return http.HttpResponse('Ocurrio un error al genera el reporte %s' % cgi.escape(html))

@login_required(login_url='/login')
def generar_pdf(request):
    factura = Factura.objects.all()

    if request.method == "POST":
        formbusqueda = RangoForm(request.POST)
        vendedor = request.POST.get('vendedor')
        
        if formbusqueda.is_valid():
            fecha_in = formbusqueda.cleaned_data['fecha_i']
            fecha_fi = formbusqueda.cleaned_data['fecha_f']
            rango = Factura.objects.filter(fecha__range=(fecha_in, fecha_fi)).filter(vendedor__pk=request.user.id)
          
            total = 0
            for expe in rango:
                total = ((expe.total) + (total))

            return write_pdf ('factura/reporte_factura.html',{'pagesize' : 'legal', 'rango' : rango, 'total': total})
            #return render_to_response ('empleados/test.html',{'rango':rango},context_instance=RequestContext(request))
        else:
            error = "Hay un error en las fechas proporcionadas"
            return render_to_response('factura/rango_reporte.html', {'error': error}, context_instance=RequestContext(request))

    return render_to_response('factura/rango_reporte.html', {'rangoform': RangoForm()}, context_instance=RequestContext(request))


def reporteventas(request, pk):
    compra = Venta.objects.get(pk=pk)
    productos = compra.venta.all()
    hora = time.strftime("%H:%M:%S")

    context = {
                "compra":compra,
                "productos":productos,
                "hora": hora
              }

    return render(
        request,
        'factura/detalle_venta.html', 
        context
        )
