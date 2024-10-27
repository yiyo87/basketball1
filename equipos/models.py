from django.db import models

# Create your models here.
class Equipo(models.Model):
    nombreEquipo = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    conferencia = models.CharField(max_length=50)
    estadio = models.CharField(max_length=50)
    anioFundacion = models.IntegerField()