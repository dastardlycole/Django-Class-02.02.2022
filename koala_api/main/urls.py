from importlib import import_module
from django.urls import path
from .views import *


urlpatterns = [
    path('songs/', song_view, name="songs"),
    path('songs/<int:song_id>/', song_change_view, name="get_one"),
    path('playlist/', playlist_view, name="playlist")
]