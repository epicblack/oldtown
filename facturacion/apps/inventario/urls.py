from django.urls import path
from apps.inventario.views import ProductoListView, ServicioListView, ProductoCreate, ServicioCreate

urlpatterns = [
    path('productos/', ProductoListView.as_view(), name='productos-list'),
    path('productos/crear/', ProductoCreate.as_view(), name='producto-crear'),
    path('servicios/', ServicioListView.as_view(), name='servicios-list'),
    path('servicios/crear/', ServicioCreate.as_view(), name='servicio-crear'),
]
