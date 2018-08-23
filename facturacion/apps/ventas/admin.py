from django.contrib import admin
from apps.ventas.models import Recibo, Orden

# Register your models here.
admin.site.register(Recibo)
admin.site.register(Orden)