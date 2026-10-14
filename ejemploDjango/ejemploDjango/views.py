#llamar las librerias para reclamar informacion y enviar respuestas
from django.http import HttpResponse,HttpRequest

#nuestro primer metodo del controlador para cargar una vista principal

def inicio(request): #Primera vista
    #devolvemos una respuesta
    return HttpResponse("Hola soy la pagina Principal")

#necesitamos ir al url para enrutarlo y mostrarlo