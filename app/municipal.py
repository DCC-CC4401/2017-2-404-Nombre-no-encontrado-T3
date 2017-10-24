from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from app.decorators import group_required
from app.functions import parseDenunciaSet
from app.models import Denuncia, User


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
    set_header = ["Tipo de Denuncia","Animal","Dirección","Herido"]

    return render(request,'muni-lista-denuncias.html',context={'set_denuncia': denunciasProcesadas,
                                                               'set_header': set_header})

@login_required()
@group_required('municipal')
def estadisticas(request):

    username = request.user.get_username()
    reportadas = Denuncia.objects.all().filter(comuna__username=username, estado="RE").count()
    consolidadas = Denuncia.objects.all().filter(comuna__username=username, estado="CO").count()
    verificadas = Denuncia.objects.all().filter(comuna__username=username, estado="VE").count()
    cerradas = Denuncia.objects.all().filter(comuna__username=username, estado="CE").count()
    desechadas = Denuncia.objects.all().filter(comuna__username=username, estado="DE").count()
    denuncias = reportadas + consolidadas + verificadas + desechadas
    numComunas = 10 #dummy
    numTotal = 100 #dummy
    #denunciasProcesadas = parseDenunciaSet(set_denuncia)

    template = loader.get_template('muni-estadisticas-ongs-ong.html')

    context = {
        'numComunas': numComunas,
        'numTotal': numTotal,
        'username': username,
        'reportadas': reportadas,
        'consolidadas': consolidadas,
        'verificadas': verificadas,
        'cerradas': cerradas,
        'desechadas': desechadas,
        'totalDen': denuncias
    }

    return HttpResponse(template.render(context, request))
