from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def plantilla(request):
    today = datetime.today().date
    context = {
        'Nombre':'Pablo',
        'Apellido': 'R.',
        'Today': today
    }
    return render(request, 'plantilla.html', context = context)






