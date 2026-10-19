from django.template import Template, Context, loader #loader.get_template()
from django.http import HttpResponse, HttpRequest
from datetime import datetime

def cursos(request):
    nombre_profesor = "Santiago"
    cursos = ["Python", "JavaScript", "C#", "C++"]

    plt = loader.get_template("index.html")
    vista = plt.render({"Nombre": nombre_profesor, "Cursos": cursos})

    return HttpResponse(vista)