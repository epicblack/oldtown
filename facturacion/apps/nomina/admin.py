from django.contrib import admin
from apps.nomina.models import Nomina, PagoNomina

class NominaAdmin(admin.ModelAdmin):
    list_display = ('persona', 'rol', 'porcentaje', 'valor')


class PagoNominaAdmin(admin.ModelAdmin):
    list_display = ('nomina', 'valor', 'fecha')


admin.site.register(Nomina, NominaAdmin)
admin.site.register(PagoNomina, PagoNominaAdmin)