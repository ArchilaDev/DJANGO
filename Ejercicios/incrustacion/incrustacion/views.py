from django.template import loader, Template
from django.http import HttpResponse, HttpRequest

#herencia

from django.shortcuts import render

#metodo del cargador
def barra(request):
    #cargador
    html = loader.get_template("index.html")
    vista = html.render()

    return HttpResponse(vista)

def herencia(request):
    return render(request, "contenido.html")
