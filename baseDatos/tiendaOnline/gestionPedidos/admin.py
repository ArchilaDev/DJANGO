from django.contrib import admin
from gestionPedidos.models import *
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    #para ver los datos en forma de tablas se usa el atributo list_display

    list_display = ("nombreC", "direccion", "email", "telefono")

    #Para buscar datos o campos 
    search_fields = ("nombreC", "direccion")

    #filtrar campos
    list_filter = ("email",) #trabajamos con tuplas

class ArticuloAdmin(admin.ModelAdmin):
    #para ver los datos en forma de tablas se usa el atributo list_display

    list_display = ("nombreArticulo", "seccion", "precio")
    search_fields = ("nombreArticulo", "precio")
    list_filter = ("seccion",)

class PedidoAdmin(admin.ModelAdmin):
    #para ver los datos en forma de tablas se usa el atributo list_display

    list_display = ("numeroP", "fecha", "estado")
    search_fields = ("numeroP", "fecha", "estado")
    list_filter = ("estado",)



#CREACION DE ¿?
admin.site.register(Cliente, ClienteAdmin) #agregamos la clase para que se vea
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Pedido, PedidoAdmin)

#FORMA MINIMALISTA DE HACERLO MAS CORTO @admin.register(Cliente) se llama decorador. el decorador es prioridad si se pone es decir global mas o menos
