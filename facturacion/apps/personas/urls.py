from django.urls import path
from apps.personas.views import PersonaListView

urlpatterns = [
    path('', PersonaListView.as_view(), name='personas-list'),
]