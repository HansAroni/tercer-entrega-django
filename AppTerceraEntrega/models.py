from django.db import models

# Create your models here.
class Empleado(models.Model):
    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    celular = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.apellido}'
    
class ProductosNuevos(models.Model):
    
    marca = models.CharField(max_length=50)
    version = models.CharField(max_length=50)
    largo = models.IntegerField()
    
class ProductosUsados(models.Model):
    
    marca = models.CharField(max_length=50)
    version = models.CharField(max_length=50)
    largo = models.IntegerField()
    
class Equipamiento(models.Model):
    
    Nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
