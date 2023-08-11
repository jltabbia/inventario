from django.db import models

# Create your models here.
class Inventario(models.Model):
    rubro=models.IntegerField(verbose_name='Rubro')
    subrubro=models.IntegerField(verbose_name='Sub-Rubro')
    codigo=models.IntegerField(verbose_name='Código')
    detalle=models.CharField(max_length=255, verbose_name='Detalle')
    
    def __str__ (self):
       return '%s %s %s %s' % (self.rubro, self.subrubro, self.codigo, self.detalle)
    
    class Meta:
        db_table = 'inventario'
        ordering = ["rubro","subrubro","codigo"]
        verbose_name_plural = "Inventario"
        verbose_name = 'Inventario'
        managed=True
    