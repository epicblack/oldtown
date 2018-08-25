from django.urls import path
from apps.inventario.views import (ProductoListView, ServicioListView,
                                   ProductoCreate, ServicioCreate,
                                   ProductoUpdate, ServicioUpdate)

urlpatterns = [
    path('productos/', ProductoListView.as_view(), name='productos-list'),
    path('productos/crear/', ProductoCreate.as_view(), name='producto-crear'),
    path('productos/editar/<int:pk>/', ProductoUpdate.as_view(),
         name='producto-editar'),
    path('servicios/', ServicioListView.as_view(), name='servicios-list'),
    path('servicios/crear/', ServicioCreate.as_view(), name='servicio-crear'),
    path('servicios/editar/<int:pk>/', ServicioUpdate.as_view(),
         name='servicio-editar'),
]
