from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, 
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)
from apps.personas.models import Persona

# Create your views here.
class PersonaListView(ListView):
    model = Persona
    template_name = 'personas/personas_list.html'  # Specify your own template name/location
    queryset = Persona.objects.all()