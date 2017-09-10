# -*- encoding: utf-8 -*-

from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Proveedor
from .forms import ProveedorForm

import csv

#Reporte pdf

from datetime import *
import xhtml2pdf.pisa as pisa
from django import http
from django.template.loader import get_template
from django.template import Context
from io import BytesIO as StringIO
import cgi


class ListaProveedores(ListView):
	model = Proveedor
	context_object_name = 'lista_proveedores'
	template_name = "proveedores/lista_proveedores.html"

class DetalleView(DetailView):
	model = Proveedor
	template_name = 'proveedores/detalle_proveedores.html'

class ActualizarView(UpdateView):
	form_class = ProveedorForm
	template_name = 'proveedores/create_update_proveedores.html'
	model = Proveedor
	success_url='/proveedores'

class CreateProveedores(CreateView):
	form_class = ProveedorForm
	template_name = 'proveedores/create_proveedores.html'
	model = Proveedor
	success_url = '/proveedores'

class EliminarView(DeleteView):
	model = Proveedor
	template_name = 'proveedores/eliminar_proveedor.html'
	success_url='/proveedores'


def write_pdf(template_src, context_dict):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = StringIO()
    pdf = pisa.pisaDocument(StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return http.HttpResponse(result.getvalue(), \
            content_type='application/pdf')
    return http.HttpResponse('Ocurrio un error al genera el reporte %s' % cgi.escape(html))


def generar_reporte_proveedores(request):
	 proveedores = Proveedor.objects.all()

	 return write_pdf ('proveedores/reporte_detalle_proveedores.html',{'pagesize' : 'legal',
	 				   'proveedores' : proveedores})
