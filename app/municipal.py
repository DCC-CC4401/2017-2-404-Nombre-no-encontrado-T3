from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from app.decorators import group_required
from app.functions import parseDenunciaSet
from app.models import Denuncia


@login_required()
@group_required('municipal')
def homeMunicipalidad(request):
    return render(request,'muni-estadisticas-ongs.html')

@login_required()
@group_required('municipal')
def listaDenuncias(request):
    username = request.user.get_username()
    set_denuncia = Denuncia.objects.all().filter(comuna__username=username)
    denunciasProcesadas = parseDenunciaSet(set_denuncia)
    set_header = ["Maltrato","Sexo","Estado","Animal","Dirección","Herido"]

    return render(request,'muni-lista-denuncias.html',context={'set_denuncia': denunciasProcesadas,
                                                               'set_header': set_header})