from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

def bienvenida(request):
    return HttpResponse("Probando una vista basada en funciones")

def hola_a_todos(request):
    return HttpResponse("Hola 😊")

def saludo(request, nombre):
    return HttpResponse(f"Hola, {nombre} Estas dentro de mi aplicación DJANGO 😎")

class BienvenidaVista(TemplateView):
    template_name = 'bienvenida.html' # Tiene que tener como nombre 'template_name' 


