"""djangoqa URL Configuration

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

from core import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$',views.perguntas_recentes,name="index"),
    url(r'^perguntas/(?P<id_pergunta>[0-9]+)/$',views.respostas,name="detalhes"),
    url(r'^perguntas/(?P<id_pergunta>[0-9]+)/excluir/$',views.excluir_pergunta),
    url(r'^perguntas/(?P<id_pergunta>[0-9]+)/detalhes/$',views.detalhes_pergunta),
    url(r'^perguntas/(?P<id_pergunta>[0-9]+)/edit/$',views.editar_pergunta),
    url(r'^respostas/(?P<id_resposta>[0-9]+)/mais_util/$',views.escolher_resposta),

    url(r'^tags/create/$',views.criar_tag,name="criar_tag")
]
