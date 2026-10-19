#Crear plantilla html ,importar
from django.template import Template, Context, loader #loader.get_template()
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

#bucles, filtros , condicionales, listas

def bucles(request):
    #simulacion de la base de datos
    fecha = datetime.now()
    nombre = "Santiago"
    apellido="Archila"

    #Crear una lista con 4 elementos de su preferencia
    cursos = ["Python", "Git", "MySQL", "PHP"]

    plt = loader.get_template('index.html')
    #dibujamos la plantilla
    vista = plt.render({"Nombre": nombre, "Apellido":apellido, "Fecha":fecha, "Lista" : cursos})#siempre usaremos diccionario para renderizar
    
    return HttpResponse(vista)