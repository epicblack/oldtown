from django.db import models
from apps.personas.models import Persona

# Create your models here.
class Referido(models.Model):
    refiere = models.ForeignKey(Persona, 
                                on_delete=models.CASCADE)
    referido = models.OneToOneField(Persona, 
                                    on_delete=models.CASCADE, 
                                    related_name='+')


class Fidelizacion(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    cantidad_servicios = models.IntegerField(default=0)
    cantidad_referidos = models.IntegerField(default=0)
    cantidad_redenciones = models.IntegerField(default=0)

    def __str__(self):
        return self.persona


class Convenio(models.Model):
    nombre_entidad = models.CharField(max_length=30)
    porcentaje = models.IntegerField(default=0)
    cerveza = models.BooleanField(default=False)
    activo = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre_entidad