from django.db import models

# Create your models here.

#Para crear las tablas se utiliza la  palabra reservada class

class Cliente(models.Model):
    #atributos - campos de tabla
    nombreC = models.CharField(max_length=50, verbose_name="Nombre Cliente")
    direccion = models.CharField(max_length=50, verbose_name="Dirrecion Cliente")
    email = models.EmailField(max_length=50, verbose_name="Email Cliente")
    telefono = models.CharField(max_length=15, verbose_name="Telefono Cliente")

class Articulo(models.Model):
    nombreArticulo = models.CharField(max_length=30)
    seccion = models.CharField(max_length=30, verbose_name="Seccion")
    precio = models.FloatField()

class Pedido(models.Model):
    numeroP = models.IntegerField( verbose_name="Numero Pedido")
    fecha = models.DateField()
    estado = models.BooleanField() #Negativo llega

