from django.urls import path
from . import views


urlpatterns = [
    path("songs/", views.songs),
    path("songs/<int:song_id>/", views.song_detail),
    path("playlists/", views.playlists),
    path("playlists/<int:item_id>/", views.playlist_detail),
]