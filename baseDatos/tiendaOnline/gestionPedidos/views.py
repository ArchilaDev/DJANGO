from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import *
# Create your views here.
def busquedaArticulo(request):
    return render(request, "busqueda_articulos.html")


def buscar(request):
    #mensaje = "Articulo buscado %r " %request.GET["txtBuscar"] reclamar el dato de busqueda por medio del input con el name = "txtBuscar"
   
    if 'txtBuscar' in request.GET: #verifica si el parametro txtBuscar esta en la solicitud
        articulo = request.GET['txtBuscar']
        articulos = Articulo.objects.filter(nombreArticulo__icontains = articulo)
    
        return render(request, "resultados.html" , \
                  {"articulos": articulos, "query":articulo})
    else:
        mensaje = "No has ingresado nada"

        return HttpResponse(mensaje)