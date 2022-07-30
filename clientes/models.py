from django.db import models

# Create your models here.

class Clientes(models.Model):
    cuil=models.CharField(max_length=15, null=False, verbose_name="CUIL/CUIT")
    nombre=models.CharField(max_length=100, null=False,verbose_name="Nombre y Apellido")
    direccion=models.CharField(max_length=150,verbose_name="Dirección")
    fecha_alta=models.DateField(auto_now=True,verbose_name="Fecha de Alta")
    localidad=models.IntegerField(default=0, verbose_name="Localidad")
    provincia=models.IntegerField(default=0,verbose_name="Provincia")
    estado=models.CharField(max_length=1,default='A',verbose_name='Estado')
