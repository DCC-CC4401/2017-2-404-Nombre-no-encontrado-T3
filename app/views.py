from django.shortcuts import render
from app.forms import *
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Animal

# Create your views here.


def home(request):
    return render(request, 'index.html')


def denuncia(request):
    if request.POST:
        form = DenunciaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Tu denuncia ha sido realizada correctamente!')
            return HttpResponseRedirect('/denuncia/')

    else:
        form = DenunciaForm()
        return render(request, 'denuncia.html', {'form' : form})


def animales(request):
    my_animals = Animal.objects.all()

    return render(request, 'lista-animales.html', {'my_animals' : my_animals})
