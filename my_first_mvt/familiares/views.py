from django.shortcuts import render
from familiares.models import Relatives

def create_relative(request):
    relative = Relatives.objects.create(name = 'Jose', age = 20, birth_date = '1900-1-1')
    context = {
        'new_relative': relative
    }
    return render(request,'new_relative.html', context = context)
