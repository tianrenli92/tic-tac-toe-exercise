from django.urls import path, include
from .views import index, new_game, load_game, show_game, mark

app_name = 'game'

urlpatterns = [
    # home page
    path('', index, name='index'),
    # create a new game, and jump to the game page
    path('new', new_game, name='new_game'),
    # check the game id and jump to the game page
    path('load', load_game, name='load_game'),
    # read the game and show it
    path('game/<int:game_id>', show_game, name='show_game'),
    # mark the game board
    path('game/<int:game_id>/mark', mark, name='mark'),
]
