from django.shortcuts import render, redirect
from app.forms import * #import
from django.http import HttpResponseRedirect
from django.contrib import messages

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
        #Denuncia.objects.all().delete()
        form = DenunciaForm()
        return render(request, 'denuncia.html', {'form' : form})
