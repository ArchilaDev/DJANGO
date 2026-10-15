#Crear plantilla html ,importar
from django.template import Template, Context
from django.http import HttpResponse, HttpRequest
from datetime import datetime
#metodo para cargar la primera plantilla
def index(request):
    #crear una variable que guardara temporalmente la ruta de busquda de la plantilla - ruta absoluta
    ruta = open("C:/Users/devel/Desktop/ESCRITORIO2/TODO/POLITECNICO/DJANGO/CodigoPy/DJANGO/ejemplosPlantillas/plantillas/plantillas/plantilla/index.html")

    #proceso de comunicacion
    plt = Template(ruta.read())

    ruta.close()


    #contexto : darle el contenido
    ctx = Context()

    #dibujamos la plantilla
    vista = plt.render(ctx) #la unica forma que muestra codigo html en python

    return HttpResponse(vista)


def variables(request):
    #simulacion de la base de datos
    fecha = datetime.now()
    nombre = "Santiago"
    apellido="Archila"

    ruta = open("C:/Users/devel/Desktop/ESCRITORIO2/TODO/POLITECNICO/DJANGO/CodigoPy/DJANGO/ejemplosPlantillas/plantillas/plantillas/plantilla/index.html")
       #proceso de comunicacion
    plt = Template(ruta.read())
    
    ruta.close()
    
    
    #contexto : darle el contenido. CREAR UN DICCIONARIO PARA MANDAR LA INFORMACION
    ctx = Context({"Nombre": nombre, "Apellido":apellido, "Fecha":fecha})
    
    #dibujamos la plantilla
    vista = plt.render(ctx) #la unica forma que muestra codigo html en python
    
    return HttpResponse(vista)