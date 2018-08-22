from django.db import models

# Create your models here.
class Rol(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Genero(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class TipoIdentificacion(models.Model):
    nombre = models.CharField(max_length=30)
    abreviacion = models.CharField(max_length=2)

    def __str__(self):
        return self.abreviacion


class Persona(models.Model):
    nombres = models.CharField(max_length=30)
    primer_apellido = models.CharField(max_length=20)
    segundo_apellido = models.CharField(max_length=10, blank=True)
    tipo_identificacion = models.ForeignKey(TipoIdentificacion, null=True, on_delete=models.SET_NULL)
    identificacion = models.IntegerField(unique=True)
    genero = models.ForeignKey(Genero, null=True, on_delete=models.SET_NULL)
    email = models.EmailField(blank=True, unique=True)
    telefono = models.IntegerField(blank=True)
    direccion = models.CharField(max_length=30, blank=True)
    nacimiento = models.DateField(null=True, blank=True)
    rol = models.ManyToManyField(Rol)
    fecha_registro = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.tipo_identificacion} {self.identificacion}'