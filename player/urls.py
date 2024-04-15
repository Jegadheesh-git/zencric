from django.urls import path
from . import views

urlpatterns = [
    path('players/all',views.getAllPlayers),
    path('players/add/',views.addPlayer),
    path('players/<int:player_id>/',views.getPlayerById),
    path('players/update/<int:player_id>/', views.updatePlayer, name='update_player_by_id'),
    path('players/delete/<int:player_id>/', views.deletePlayer, name='delete_player_by_id'),
]