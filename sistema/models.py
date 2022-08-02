from statistics import mode
from django.db import models

class Provincias(models.Model):
    codigo=models.IntegerField(verbose_name='Código')
    nombre=models.CharField(max_length=50, verbose_name='Provincia')
    
class Localidades(models.Model):
    codigo_provincia=models.IntegerField(verbose_name='Código Provincia')
    codigo_localidad=models.IntegerField(verbose_name='Código Localidad')
    nombre_localidad=models.CharField(max_length=100, verbose_name='Localidad')
    
