from django.contrib import admin
from apps.personas.models import (Rol, TipoIdentificacion, 
                                  Genero, Persona)

# Register your models here.
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('primer_apellido',
                    'segundo_apellido',
                    'nombres', 
                    'tipo_identificacion',
                    'identificacion', 
                    'email')

    search_fields = ('identificacion', 'primer_apellido', 'segundo_apellido')

admin.site.register(Rol)
admin.site.register(Genero)
admin.site.register(TipoIdentificacion)
admin.site.register(Persona, PersonaAdmin)