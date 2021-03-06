"""ProjectoCholito URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin

from app import views, auth, municipal, usuario #se agrego usuario al import

urlpatterns = [
    url(r'^login/$', auth.login_view, name ='login'),
    url(r'^signup/$', auth.signup, name ='signup'),
    url(r'^logout/$', auth.logout_view, name ='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^home/', views.home, name='home'),
    url(r'^denuncia/', views.denuncia, name='denuncia'),
    url(r'^signup2/', auth.signupmunicipal, name = 'signupmunicipal'),
    url(r'^municipalidad/denuncia/modify/(?P<id>\w{0,50})/$', municipal.modifyDenuncia, name = 'modifyDenuncia'),
    url(r'^municipalidad/denuncia/view/(?P<id>\w{0,50})/$', municipal.viewDenuncia, name = 'viewDenuncia'),
    url(r'^municipalidad/estadisticas/', municipal.estadisticas, name='estadisticas'),
    url(r'^municipalidad/denuncias/', municipal.listaDenuncias, name = 'listaDenuncias'),
    url(r'^municipalidad/', municipal.homeMunicipalidad, name = 'homeMunicipalidad'),
    url(r'^registermiddlepage/', auth.registerbuttonpage, name = 'registerbuttonpage' ),
    url(r'^usuario/', usuario.homeUsuario, name = 'homeUsuario'), #esta linea fue agregada
    url(r'^animales/', views.animales, name='animales'),
    url(r'$', views.home, name='home'),

]

