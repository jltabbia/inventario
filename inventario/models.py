from email.policy import default
from django.db import models
from django.forms import CharField, DateField, IntegerField

# Create your models here.

class Inventario(models.Model):
    __tablename__ = 'inventario'
    codigo=models.IntegerField()
    detalle=models.CharField(max_length=150, null=False)
    stock=models.IntegerField(default='0')
    stock_minimo=models.IntegerField(default='0')
    ultima_compra=models.DateField(null=True)
    observaciones=models.CharField(max_length=150, null=True)

    def __str__ (self, codigo,detalle,stock,stock_minimo,ultima_compra, observaciones):
        self.codigo=codigo
        self.detalle=detalle
        self.stock=stock
        self.stock_minimo=stock_minimo
        self.ultima_compra=ultima_compra
        self.observaciones=observaciones
        return (codigo,detalle,stock,stock_minimo,ultima_compra,observaciones)

class Clientes(models.Model):
    cuil=models.CharField(max_length=15, null=False)
    nombre=models.CharField(max_length=100, null=False)
    direccion=models.CharField(max_length=150)

    def __str__(self, cuil, nombre, direccion):
        self.cuil=cuil
        self.nombre=nombre
        self.direccion=direccion
        return (cuil, nombre, direccion)