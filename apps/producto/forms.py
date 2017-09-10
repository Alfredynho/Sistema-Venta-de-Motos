#encoding:utf-8
from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
	class Meta:
		model = Producto
		exclude = ('marca',)



class CrearProductoForm(forms.ModelForm):
	class Meta:
		model = Producto
		exclude = ('marca',)
		fields = "__all__"

