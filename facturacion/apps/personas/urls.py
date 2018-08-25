from django.urls import path
from apps.personas.views import PersonaListView, PersonaCreate, PersonaUpdate


urlpatterns = [
    path('', PersonaListView.as_view(), name='personas-list'),
    path('nueva/', PersonaCreate.as_view(), name='personas-create'),
    path('editar/<int:pk>/', PersonaUpdate.as_view(), name='personas-editar'),
]
