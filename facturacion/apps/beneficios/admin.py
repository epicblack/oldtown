from django.contrib import admin
from apps.beneficios.models import (Referido, Fidelizacion,
                                    Convenio)

# Register your models here.
class ReferidoAdmin(admin.ModelAdmin):
    list_display = ('refiere',
                    'referido')


class ConvenioAdmin(admin.ModelAdmin):
    list_display = ('nombre_entidad',
                    'porcentaje',
                    'cerveza',
                    'activo')

admin.site.register(Referido, ReferidoAdmin)
admin.site.register(Fidelizacion)
admin.site.register(Convenio, ConvenioAdmin)
