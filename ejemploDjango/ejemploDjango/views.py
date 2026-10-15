#llamar las librerias para reclamar informacion y enviar respuestas
from django.http import HttpResponse,HttpRequest

#nuestro primer metodo del controlador para cargar una vista principal
#importar la libreria de fecha y hora

from datetime import datetime


def inicio(request): #Primera vista
    #devolvemos una respuesta
    return HttpResponse("Hola soy la pagina Principal")

#necesitamos ir al url para enrutarlo y mostrarlo

#metodo para mostrar la fecha y hora dinamicamente

def fechaSistema(request): #Por que request?
    #variable para instacian el objeto fecha y hora
    fechaActual = datetime.now()

    #variable para mandar algo de diseño html
    html = """
            <html>
                <body>
                    <h1> En mi sitema la hora y fecha actual es: </h1> %s
                </body>
            </html>
            """ % fechaActual
    return HttpResponse(html)

#url amigable, parametros en url

def cacularEdad(request, anio):
    #variable con dato quemado de edad
    edadActual = 22
    periodo = anio-2026

    edadFutura = edadActual + periodo

    html = """
            <html>
                    <body style = "background-color: blue;">
                        <h1>Tiempo de programador </h1>
                        <p>Para el año %s </p>
                        <p>Santiago va a tener %s años de experiencia en el desarrollo</p>
                    </body>
                </html>
            """ % (anio,edadFutura) #cuando son mas de un parametro necesitamos enviarlo con parentesis

    return HttpResponse(html)