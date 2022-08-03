from django.db import models

# Create your models here.
class Provincias(models.Model):
    codigo=models.IntegerField(verbose_name='Código')
    nombre=models.CharField(max_length=50, verbose_name='Provincia')
    
class Localidades(models.Model):
    codigo_provincia=models.IntegerField(verbose_name='Código Provincia')
    codigo_localidad=models.IntegerField(verbose_name='Código Localidad')
    nombre_localidad=models.CharField(max_length=100, verbose_name='Localidad')
    
class Rubros(models.Model):
    id_rubro=models.IntegerField(verbose_name="Id Rubro")
    detalle=models.CharField(max_length=100, null=False, verbose_name="Detalle")
    id_rubro_padre=models.IntegerField()
    