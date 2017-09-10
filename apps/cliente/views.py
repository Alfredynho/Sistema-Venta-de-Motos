# -*- encoding: utf-8 -*-

from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Cliente
from .forms import ClienteForm

import csv

#Reporte pdf

from datetime import *
import xhtml2pdf.pisa as pisa
from django import http
from django.template.loader import get_template
from django.template import Context
from io import BytesIO as StringIO
import cgi


class ListaClientes(ListView):
	model = Cliente
	context_object_name = 'lista_clientes'
	template_name = "clientes/lista_clientes.html"

class DetalleView(DetailView):
	model = Cliente
	template_name = 'clientes/detalle_clientes.html'

class ActualizarView(UpdateView):
	form_class = ClienteForm
	template_name = 'clientes/create_update_clientes.html'
	model = Cliente
	success_url='/clientes'

class CreateClientes(CreateView):
	form_class = ClienteForm
	template_name = 'clientes/create_clientes.html'
	model = Cliente
	success_url = '/clientes'

class EliminarView(DeleteView):
	model = Cliente
	template_name = 'clientes/eliminar_cliente.html'
	success_url='/clientes'


def write_pdf(template_src, context_dict):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = StringIO()
    pdf = pisa.pisaDocument(StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return http.HttpResponse(result.getvalue(), \
            content_type='application/pdf')
    return http.HttpResponse('Ocurrio un error al genera el reporte %s' % cgi.escape(html))


def generar_reporte_clientes(request):
	 clientes = Cliente.objects.all()

	 return write_pdf ('clientes/reporte_detalle_clientes.html',{'pagesize' : 'legal',
	 				   'clientes' : clientes})
