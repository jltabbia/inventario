from django.db import models

# Create your models here.
    
class Rubros(models.Model):
    detalle=models.CharField(max_length=100, null=False, verbose_name="Detalle")
    
class Subrubros(models.Model):
    detalle=models.CharField(max_length=50,null=False, verbose_name="Detalle")
    id_rubro=models.IntegerField()
    
    