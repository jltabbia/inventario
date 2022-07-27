from email.policy import default
from django.db import models
from django.forms import CharField, DateField, IntegerField

# Create your models here.

class Inventario(models.Model):
    codigo=models.IntegerField()
    detalle=models.CharField(max_length=150, null=False)
    stock=models.IntegerField(default='0')
    stock_minimo=models.IntegerField(default='0')
    ultima_compra=models.DateField(null=True)
    observaciones=models.CharField(max_length=150, null=True)


class Clientes(models.Model):
    cuil=models.CharField(max_length=15, null=False)
    nombre=models.CharField(max_length=100, null=False)
    direccion=models.CharField(max_length=150)
