from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)
from apps.inventario.models import Producto, Servicio
from apps.inventario.forms import ProductoForm, ServicioForm

# Create your views here.


class ProductoListView(ListView):
    model = Producto
    # Specify your own template name/location
    template_name = 'inventario/producto_list.html'
    queryset = Producto.objects.all()


class ProductoCreate(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'inventario/producto_crear.html'
    success_url = reverse_lazy('productos-list')


class ProductoUpdate(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'inventario/producto_crear.html'
    success_url = reverse_lazy('productos-list')


class ServicioListView(ListView):
    model = Servicio
    # Specify your own template name/location
    template_name = 'inventario/servicio_list.html'

    queryset = Servicio.objects.all()


class ServicioCreate(CreateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'inventario/servicio_crear.html'
    success_url = reverse_lazy('servicios-list')


class ServicioUpdate(UpdateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'inventario/servicio_crear.html'
    success_url = reverse_lazy('servicios-list')
