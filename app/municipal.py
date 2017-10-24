from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from app.decorators import group_required
from app.forms import DenunciaForm, ModifyDenunciaForm
from app.models import Denuncia


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
