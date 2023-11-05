"""
URL configuration for FirstProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login/', views.login_user, name="login"),
    path('logout', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
    path('addmoney/' , views.addmoney, name="addmoney"),
    path('usrdetails/', views.usrdetails, name="usrdetails"),
    path('admin_page', views.admin_page, name="admin_page"),
    path('delete_team/<str:team_name>/', views.delete_team, name='delete_team'),
    path('delete_game/<str:game_identifier>/', views.delete_game, name='delete_game'),
    path('search_games/', views.search_games, name='search_games'),
    path('update_game_odds/<int:game_id>/', views.update_game_odds, name='update_game_odds'),
    path('add_team/', views.add_team, name='add_team'),
    path('addadmin/', views.addadmin, name="addadmin"),
    path('managebets/', views.managebets, name="managebets"),
    path('manageusers/', views.manageusers, name="manageusers"),
    path('user_bets/', views.user_bets, name='user_bets')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)