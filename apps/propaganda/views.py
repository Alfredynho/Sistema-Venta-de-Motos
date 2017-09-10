# -*- encoding: utf-8 -*-

from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Propaganda
from .forms import PropagandaForm


# ListaPropagandas, 
# DetalleView,
# ActualizarView,
# CreatePropagandas,
# EliminarView


class ListaPropagandas(ListView):
	model = Propaganda
	context_object_name = 'lista_propagandas'
	template_name = 'propagandas/listar_propagandas.html'


class DetalleView(DetailView):
	model = Propaganda
	template_name = 'propagandas/detalle_propaganda.html'


class ActualizarView(UpdateView):
	form_class = PropagandaForm
	template_name = 'propagandas/update_propaganda.html'
	model = Propaganda
	success_url = '/propagandas'

class CreatePropagandas(CreateView):
	form_class = PropagandaForm
	template_name = 'propagandas/create_propaganda.html'
	model = Propaganda
	success_url = '/propagandas'


class EliminarView(DeleteView):
	model = Propaganda
	template_name = 'propagandas/eliminar_propaganda.html'
	success_url = '/propagandas'
