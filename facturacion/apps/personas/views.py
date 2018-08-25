from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)
from apps.personas.models import Persona
from apps.personas.forms import PersonaForm
# Create your views here.


class PersonaListView(ListView):
    model = Persona
    queryset = Persona.objects.filter(
        rol__nombre='Cliente').order_by('primer_apellido')
    context_object_name = 'personas'
    template_name = 'personas/personas_list.html'


class PersonaCreate(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'personas/personas_crear.html'
    success_url = reverse_lazy('personas-list')


class PersonaUpdate(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'personas/personas_crear.html'
    success_url = reverse_lazy('personas-list')
