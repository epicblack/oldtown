from django.db import models
from apps.personas.models import Persona
from apps.inventario.models import Producto, Servicio
from apps.beneficios.models import Referido, Convenio

# Create your models here.
class Recibo(models.Model):
    barbero = models.ForeignKey(Persona, null=True, on_delete=models.SET_NULL)
    cliente = models.OneToOneField(Persona, null=True, on_delete=models.SET_NULL, related_name='+')
    bebida = models.BooleanField(default=True)
    referido = models.OneToOneField(Persona, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
    convenio = models.ForeignKey(Convenio, null=True, blank=True, on_delete=models.SET_NULL)
    datetime = models.DateTimeField(auto_now=True)
    total = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'Recibo: {self.id} | Barbero: {self.barbero} | Cliente {self.cliente} | {self.total}'

class Orden(models.Model):
    recibo = models.ForeignKey(Recibo, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, null=True, blank=True, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, null=True, blank=True, on_delete=models.CASCADE)
    venta = models.BooleanField(default=True)

    def check_stock(self):
        return Producto.objects.get(id=self.producto).values('cantidad')

    def __str__(self):
        return f'Recibo: {self.recibo} | Producto: {self.producto} | Servicio: {self.servicio}'