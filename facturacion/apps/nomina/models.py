from django.db import models
from apps.personas.models import Persona, Rol

# Create your models here.
class Nomina(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, null=True, on_delete=models.SET_NULL)
    porcentaje = models.BooleanField(default=True)
    valor = models.IntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.persona}'


class PagoNomina(models.Model):
    nomina = models.ForeignKey(Nomina, on_delete=models.CASCADE)
    valor = models.IntegerField()
    fecha = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.nomina} | Valor: {self.valor} | Fecha: {self.fecha}'