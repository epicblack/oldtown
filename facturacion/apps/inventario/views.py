from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, 
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)
from apps.inventario.models import Producto, Servicio

# Create your views here.
class ProductoListView(ListView):
    model = Producto
    template_name = 'inventario/producto_list.html'  # Specify your own template name/location
    queryset = Producto.objects.all()

# Create your views here.
class ServicioListView(ListView):
    model = Servicio
    template_name = 'inventario/servicio_list.html'  # Specify your own template name/location

    queryset = Servicio.objects.all()

    # def get_queryset(self):
    #     return Servicio.objects.order_by('-nombre')