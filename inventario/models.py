from email.policy import default
from django.db import models

# Create your models here.

class Inventario(models.Model):
    codigo=models.CharField(max_length=6, null=False, verbose_name="Código")
    detalle=models.CharField(max_length=150, null=False,verbose_name="Detalle")
    stock=models.IntegerField(default='0',verbose_name="Stock")
    stock_minimo=models.IntegerField(default='0', verbose_name="Stock Mínimo")
    ultima_compra=models.DateTimeField(null=True, verbose_name="Ultima Compra")
    observaciones=models.CharField(max_length=150, null=True, verbose_name="Observaciones")


class Clientes(models.Model):
    cuil=models.CharField(max_length=15, null=False)
    nombre=models.CharField(max_length=100, null=False)
    direccion=models.CharField(max_length=150)
