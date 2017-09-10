from .models import * # Change as necessary
from django.forms import ModelForm
from django import forms

# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response as render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.utils import timezone
from django.views.generic import TemplateView
from django.core import serializers
from django.db import connection
import json
# Create your views here.
from .models import Venta, DetalleVenta
from apps.cliente.models import Cliente
from apps.producto.models import Producto

from apps.empleado.models import Empleado

from django.core.urlresolvers import reverse_lazy, reverse


from django.db import transaction
from django.contrib import messages
from django.views.generic import ListView,TemplateView, CreateView
from django.template import RequestContext as ctx
from datetime import datetime

#reporte pdf
from django.http import HttpResponseRedirect
from datetime import *

from django import http
from django.template.loader import get_template
from django.template import Context

class RangoForm (forms.Form):
    fecha_i = forms.DateField(widget = forms.TextInput(attrs={'class':'form-control', 'id':'Fecha_i', 'data-date-format':'dd/mm/yyyy'}))
    fecha_f = forms.DateField(widget = forms.TextInput(attrs={'class':'form-control', 'id':'Fecha_f', 'data-date-format':'dd/mm/yyyy'}))
    
