from django.shortcuts import render, redirect
from app.forms import *
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, 'index.html')


def denuncia(request):
    if request.POST:
        form = DenunciaForm(request.POST)

        tipo = request.POST.get('tipo')
        sexo = request.POST.get('sexo')
        color = request.POST.get('color')
        herido = request.POST.get('herido')
        maltrato = request.POST.get('maltrato')
        calle = request.POST.get('calle')
        comuna = request.POST.get('comuna')
        comentario = request.POST.get('comentario')
        estado = request.POST.get('estado')

        denuncia_obj = Denuncia(tipo=tipo, sexo=sexo, color=color, herido=herido, maltrato=maltrato, calle=calle,
                                comuna=comuna, comentario=comentario, estado=estado)
        denuncia_obj.save()
        messages.info(request, 'Tu denuncia ha sido realizada correctamente!')
        return HttpResponseRedirect('/denuncia/')

    else:
        form = DenunciaForm()
        return render(request, 'denuncia.html', {'form' : form})
