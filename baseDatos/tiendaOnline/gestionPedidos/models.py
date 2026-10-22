from django.db import models

# Create your models here.

#Para crear las tablas se utiliza la  palabra reservada class

class Cliente(models.Model):
    #atributos - campos de tabla
    nombreC = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    telefono = models.CharField(max_length=15)

class Articulo(models.Model):
    nombreArticulo = models.CharField(max_length=30)
    seccion = models.CharField(max_length=30)
    precio = models.FloatField()

class Pedido(models.Model):
    numeroP = models.IntegerField()
    fecha = models.DateField()
    estado = models.BooleanField() #Negativo llega

