# -*- encoding: utf-8 -*-

from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Empleado
from .forms import EmpleadoForm

from datetime import *
import xhtml2pdf.pisa as pisa
from django import http
from django.template.loader import get_template
from django.template import Context
from io import BytesIO as StringIO
import cgi


class ListaEmpleados(ListView):
	model = Empleado
	context_object_name = 'lista_empleados'
	template_name = "empleados/lista_empleados.html"

class DetalleView(DetailView):
	model = Empleado
	template_name = 'empleados/detalle_empleados.html'

class ActualizarView(UpdateView):
	form_class = EmpleadoForm
	template_name = 'empleados/create_update_empleados.html'
	model = Empleado
	success_url='/empleados'

class CreateEmpleados(CreateView):
	form_class = EmpleadoForm
	template_name = 'empleados/create_empleado.html'
	model = Empleado
	success_url = '/empleados'

class EliminarView(DeleteView):
	model = Empleado
	template_name = 'empleados/eliminar_empleado.html'
	success_url='/empleados'


def write_pdf(template_src, context_dict):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = StringIO()
    pdf = pisa.pisaDocument(StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return http.HttpResponse(result.getvalue(), \
            content_type='application/pdf')
    return http.HttpResponse('Ocurrio un error al genera el reporte %s' % cgi.escape(html))


def generar_reporte_empleados(request):
	 empleados = Empleado.objects.all()

	 return write_pdf ('empleados/reporte_detalle_empleados.html',{'pagesize' : 'legal',
	 				   'empleados' : empleados})
