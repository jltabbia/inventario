from django.db import models

class Provincias(models.Model):
    codigo=models.IntegerField(verbose_name='Código')
    nombre=models.CharField(max_length=50, verbose_name='Provincia')
    def __str__ (self):
       return '%s %s' % (self.codigo, self.nombre)
    
    class Meta:
        db_table = 'provincias'
        ordering = ["codigo","nombre"]
        verbose_name_plural = "Provincias"
        verbose_name = 'Provincias'
        managed=True
    
class Localidades(models.Model):
    codigo_provincia=models.ForeignKey(Provincias, on_delete=models.CASCADE, verbose_name='Provincia')
    codigo_localidad=models.IntegerField(verbose_name='Código Localidad')
    nombre_localidad=models.CharField(max_length=100, verbose_name='Localidad')
    
    def __str__ (self):
       return '%s %s %s' % (self.codigo_provincia, self.codigo_localidad, self.nombre_localidad)
    
    class Meta:
        db_table = 'localidades'
        ordering = ["codigo_provincia","codigo_localidad","nombre_localidad"]
        verbose_name_plural = "Localidades"
        verbose_name = 'Localidades'
        managed=True
        
class Rubros(models.Model):
    id=models.IntegerField(verbose_name="Id Rubro", primary_key=True)
    detalle=models.CharField(max_length=100, null=False, verbose_name="Detalle")
   
    def __str__ (self):
       return '%s %s' % (self.id, self.detalle)
    
    class Meta:
        db_table = 'rubros'
        ordering = ["id","detalle"]
        verbose_name_plural = "Rubros"
        verbose_name = 'Rubros'
        managed=True
        
class Subrubros(models.Model):
    id=models.IntegerField(verbose_name="Id Sub-Rubro", primary_key=True)
    id_rubro=models.ForeignKey(Rubros, on_delete=models.CASCADE, verbose_name='Rubros')
    detalle=models.CharField(max_length=100, null=False, verbose_name="Detalle")
   
    def __str__ (self):
       return '%s %s' % (self.id, self.id_rubro, self.detalle)
    
    class Meta:
        db_table = 'subrubros'
        ordering = ["id_rubro", "id", "detalle"]
        verbose_name_plural = "SubRubros"
        verbose_name = 'SubRubros'
        managed=True
        