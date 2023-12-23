"""
URL configuration for GameStore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from GameStore import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Web Services
    path('ws/modalidade/delete', views.del_all_modalidade),
    path('ws/modalidade/delete/<int:id>', views.del_modalidade),
    path('ws/modalidade/get/<int:id>', views.get_modalidadeid),
    path('ws/modalidade/get', views.get_all_modalidade),
    path('ws/modalidade/update/<int:id>', views.update_modalidade),
    path('ws/modalidade/post', views.post_modalidade),

    # Web Services for Liga
    path('ws/liga/delete', views.del_all_liga),
    path('ws/liga/delete/<int:id>', views.del_liga),
    path('ws/liga/get/<int:id>', views.get_ligaid),
    path('ws/liga/get', views.get_all_liga),
    path('ws/liga/update/<int:id>', views.update_liga),
    path('ws/liga/post', views.post_liga),
    path('ws/liga/ligaByModalidade/<int:id>', views.ligaByModalidade),

    # Web Services for Grupo
    path('ws/grupo/delete', views.del_all_grupo),
    path('ws/grupo/delete/<int:id>', views.del_grupo),
    path('ws/grupo/get/<int:id>', views.get_grupoid),
    path('ws/grupo/get', views.get_all_grupo),
    path('ws/grupo/update/<int:id>', views.update_grupo),
    path('ws/grupo/post', views.post_grupo),

    # Web Services for Equipa

    path('ws/equipa/delete', views.del_all_equipa),
    path('ws/equipa/delete/<int:id>', views.del_equipa),
    path('ws/equipa/get/<int:id>', views.get_equipaid),
    path('ws/equipa/get', views.get_all_equipa),
    path('ws/equipa/getByModalidade/<int:id>', views.getByModalidade),
    path('ws/equipa/update/<int:id>', views.update_equipa),
    path('ws/equipa/post', views.post_equipa),
    path('ws/equipa/get/equipaByLiga/<int:id>', views.equipaByLiga),

    # Web Services for Jogador
    path('ws/jogador/get/byModalidade/<int:id>', views.jogadorByModalidade),
    path('ws/jogador/delete', views.del_all_jogador),
    path('ws/jogador/delete/<int:id>', views.del_jogador),
    path('ws/jogador/get/<int:id>', views.get_jogadorid),
    path('ws/jogador/get', views.get_all_jogador),
    path('ws/jogador/update/<int:id>', views.update_jogador),
    path('ws/jogador/post', views.post_jogador),
    path('ws/jogador/get/jogadorByLiga/<int:id>', views.jogadorByLiga),

    # Web Services for Jogo
    path('ws/jogo/delete', views.del_all_jogo),
    path('ws/jogo/delete/<int:id>', views.del_jogo),
    path('ws/jogo/get/<int:id>', views.get_jogoid),
    path('ws/jogo/get', views.get_all_jogo),
    path('ws/jogo/getEventos/<int:id>', views.eventos_jogo),
    path('ws/jogo/update/<int:id>', views.update_jogo),
    path('ws/jogo/post', views.post_jogo),

    # Web Services for Evento
    path('ws/evento/delete', views.del_all_evento),
    path('ws/evento/delete/<int:id>', views.del_evento),
    path('ws/evento/get/<int:id>', views.get_eventoid),
    path('ws/evento/get', views.get_all_evento),
    path('ws/evento/update/<int:id>', views.update_evento),
    path('ws/evento/post', views.post_evento),
    path('ws/evento/get/jogador/<int:id>', views.eventos_jogador),

    # Web Services for Classificacao
    path('ws/classificacao/delete', views.del_all_classificacao),
    path('ws/classificacao/delete/<int:id>', views.del_classificacao),
    path('ws/classificacao/get/<int:id>', views.get_classificacaoid),
    path('ws/classificacao/get', views.get_all_classificacao),
    path('ws/classificacao/update/<int:id>', views.update_classificacao),
    path('ws/classificacao/post', views.post_classificacao),

    # Web Services for User
    path('ws/user/delete', views.del_all_user),
    path('ws/user/delete/<int:id>', views.del_user),
    path('ws/user/get/<int:id>', views.get_userid),
    path('ws/user/get', views.get_all_user),
    path('ws/user/update/<int:id>', views.update_user),
    path('ws/user/post', views.post_user),

    # Web Services for FantasyTeam
    path('ws/fantasyteam/delete', views.del_all_fantasyteam),
    path('ws/fantasyteam/delete/<int:id>', views.del_fantasyteam),
    path('ws/fantasyteam/get/<int:id>', views.get_fantasyteamid),
    path('ws/fantasyteam/get', views.get_all_fantasyteam),
    path('ws/fantasyteam/update/<int:id>', views.update_fantasyteam),
    path('ws/fantasyteam/post', views.post_fantasyteam),

    path('ws/modalidade/getByname/<str:id>', views.get_modalidadeByName),
    path('ws/jogador/jogadorByModalidade/<int:id>', views.jogadorByModalidade),
    path('ws/user/getByName/<str:name>', views.getByName),
    path('ws/fantasyteam/getByuser/<int:id>', views.getByuser),
    path('ws/fantasyteam/fantaByModalidade/<str:id>', views.fantaByModalidade),
]
