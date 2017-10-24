from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render, redirect

from app.decorators import group_required
from app.forms import DenunciaForm, ModifyDenunciaForm
from app.models import Denuncia
from django.template import loader

from app.models import Denuncia, User



@login_required()
@group_required('municipal')
def homeMunicipalidad(request):
    return render(request, 'muni-estadisticas-ongs.html')


@login_required()
@group_required('municipal')
def listaDenuncias(request):
    username = request.user.get_username()
    set_denuncia = Denuncia.objects.all().filter(comuna__username=username)
    set_header = ["Tipo de Denuncia", "Animal", "Dirección", "Herido"]
    return render(request, 'muni-lista-denuncias.html', context={'set_denuncia': set_denuncia,
                                                                 'set_header': set_header})


@login_required()
@group_required('municipal')
def viewDenuncia(request, id):
    den = Denuncia.objects.all().get(id=id)
    return render(request, 'vista-denuncia-muni.html', context={'denuncia': den})



@login_required()
@group_required('municipal')
def modifyDenuncia(request, id):
    den = Denuncia.objects.all().get(id=id)
    print(den.comuna.first_name)
    form = ModifyDenunciaForm(request.POST or None, instance=den)
    if form.is_valid():
        form.save()
        return render(request, 'vista-denuncia-muni.html', context={'denuncia': den})
    return render(request, 'modifyDenuncia.html', {'form': form})


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

