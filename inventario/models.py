from django.db import models

# Create your models here.

class Inventario(models.Model):
    codigo=models.CharField(max_length=6, null=False, verbose_name="Código")
    detalle=models.CharField(max_length=150, null=False,verbose_name="Detalle")
    stock=models.IntegerField(default='0',verbose_name="Stock")
    stock_minimo=models.IntegerField(default='0', verbose_name="Stock Mínimo")
    ultima_compra=models.DateField(null=True, verbose_name="Ultima Compra",blank=True)
    observaciones=models.CharField(max_length=150, null=True, verbose_name="Observaciones",default="",blank=True)
