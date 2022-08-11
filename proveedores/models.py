from email.policy import default
from django.db import models

# Create your models here.
class Proveedores(models.Model):
    nombre=models.CharField(max_length=100)
    cuit_cuil=models.CharField(max_length=15)
    domicilio=models.CharField(max_length=100)
    provincia=models.IntegerField()
    localidad=models.IntegerField()
    telefono=models.CharField(max_length=20)
    contacto=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    observaciones=models.TextField(max_length=256)
    