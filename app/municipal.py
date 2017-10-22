from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from app.decorators import group_required

@login_required()
@group_required('municipal')
def homeMunicipalidad(request):
    return render(request,'muni-estadisticas-ongs.html')