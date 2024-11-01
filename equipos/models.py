from django.db import models
from django.utils import timezone

# Create your models here.
class Equipo(models.Model):
    nombreEquipo = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    conferencia = models.CharField(max_length=50)
    estadio = models.CharField(max_length=50)
    anioFundacion = models.IntegerField()

    def __str__(self):
        return self.nombreEquipo


class Jugador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    posicion = models.CharField(max_length=50)
    altura = models.CharField(max_length=50)
    peso = models.CharField(max_length=50)
    edad = models.IntegerField()
    


    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Partido(models.Model):
    fecha = models.DateTimeField(default=timezone.now)
    hora = models.IntegerField(default=0)
    estadio = models.CharField(max_length=255, default='Estadio desconocido')
