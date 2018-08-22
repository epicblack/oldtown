from django.contrib import admin
from apps.inventario.models import Producto, Servicio, Unidad

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'presentacion', 'unidad', 'precio_compra', 'precio_venta', 'cantidad')

class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio_venta')

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Unidad)
admin.site.register(Servicio, ServicioAdmin)
