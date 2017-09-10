from django.shortcuts import render
from django.views.generic import ListView
from apps.repuesto.models import Repuesto


class RepuestoSucursalListView(ListView): 
	context_object_name = 'repuestos'
	template_name = 'inventario/inventario_list_repuestos.html'

	def get_queryset(self):


		sucursal_id = self.kwargs['pk']
		sucursal = Sucursal.objects.get(id=sucursal_id)
		
		_repuestos = Repuesto.objects.filter(sucursal=sucursal)
		return _repuestos

	def get_context_data(self,**kwargs):

		context = super(RepuestoSucursalListView,self).get_context_data(**kwargs)
		sucursal_id = self.kwargs['pk']
		sucursal = Sucursal.objects.get(id=sucursal_id)
		context['sucursal'] = sucursal
		context['repuestos'] = Repuesto.objects.all()
		
		return context



class RepuestosListSucursal(ListView):

	model = Repuesto
	context_object_name = 'sucursal_repuestos'
	template_name = 'inventario/inventario_sucursal_repuesto.html'