from django.urls import path
from apps.personas.views import PersonaListView, PersonaCreate


urlpatterns = [
    path('', PersonaListView.as_view(), name='personas-list'),
    path('nueva/', PersonaCreate.as_view(), name='personas-create'),
]
