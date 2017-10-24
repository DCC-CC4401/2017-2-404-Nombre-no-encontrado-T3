#este archivo fue agregado
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from app.decorators import group_required
@login_required()
@group_required('usuario')
def homeUsuario(request):
    return render(request,'usuario-home.html')