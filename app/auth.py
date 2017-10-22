from app.forms import SignUpForm, SignUpFormMunicipalUser
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, Permission, User

municipalgroup, created = Group.objects.get_or_create(name='municipal')
normalusergroup, created = Group.objects.get_or_create(name='usuario')
users = User.objects.select_related('profile')

def registerbuttonpage(request):
    return render(request, "registerbuttonpage.html")


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            User.objects.get(username=username).groups.add(normalusergroup)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registrate.html', {'form': form})


def signupmunicipal(request):
    if request.method == 'POST':
        form = SignUpFormMunicipalUser(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            new_val = {'is_municipal': True}
            users.get(username=username).groups.add(municipalgroup)
            print(users.get(username=username).profile)
            users.update_or_create(username=username, defaults=new_val)
            login(request, user)
            return redirect('homeMunicipalidad')
    else:
        form = SignUpFormMunicipalUser()
    return render(request, 'registrarMunicipal.html', {'form': form})


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    login(request, user)
    if users.values_list('is_municipal', flat=True).get(username=username):
        return redirect('homeMunicipalidad')
    else:
        return redirect('home')


def logout_view(request):
    logout(request)
    return redirect('login')
