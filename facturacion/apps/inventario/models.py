from django.db import models

# Create your models here.
class Unidad(models.Model):
    nombre = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField()
    presentacion = models.IntegerField()
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)
    precio_compra = models.IntegerField()
    precio_venta = models.IntegerField()
    cantidad = models.IntegerField()

    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=200)
    precio_venta = models.IntegerField()

    def __str__(self):
        return self.nombre