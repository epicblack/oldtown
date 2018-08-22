from django.urls import path
from apps.inventario.views import ProductoListView, ServicioListView

urlpatterns = [
    path('productos/', ProductoListView.as_view(), name='productos-list'),
    path('servicios/', ServicioListView.as_view(), name='servicios-list'),
]