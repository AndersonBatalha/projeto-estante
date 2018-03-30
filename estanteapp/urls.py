"""estanteapp URL Configuration

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

from estanteapp.views import *

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^professor/cadastro$', CadastroProfessorView.as_view(), name='cadastro_professor'),
    url(r'^aluno/cadastro$', CadastroAlunoView.as_view(), name='cadastro_aluno'),
    url(r'^autor/cadastro$', CadastroAutorView.as_view(), name='cadastro_autor'),
    url(r'^autor/lista$', ListaAutorView.as_view(), name='lista_autor'),
    url(r'^autor/edicao/(?P<id>\d+)', EdicaoAutorView.as_view(), name='edicao_autor'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]
