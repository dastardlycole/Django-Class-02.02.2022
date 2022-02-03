from operator import mod
from rest_framework import serializers
from main.models import Song, Playlist

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        # fields = '__all__'
        fields = ['id','title','artist', 'publish_date', 'date_created']


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'