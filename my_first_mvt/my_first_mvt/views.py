from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def saludo(request):
    return HttpResponse('Hola mundo')

def dia_de_hoy(request):
    hoy = datetime.today().date()
    return HttpResponse(f'Hoy es {hoy}')

def saludo_nombre(request, nombre):
        return HttpResponse(f'Hola {nombre}')

def nacimiento(request, edad):
    anio_actual = datetime.today().year
    anio = anio_actual - edad
    #anio = edad
    return HttpResponse(f'Naciste en: {anio}')

def plantilla(request):
    return render(request, 'plantilla.html', context = {})






