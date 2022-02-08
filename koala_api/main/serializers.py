from rest_framework import serializers

from main.models import PlayList, Song


class SongSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Song
        fields = '__all__'
        
        

class PlayListSerializer(serializers.ModelSerializer):
    song_detail = serializers.ReadOnlyField()
    
    class Meta:
        model = PlayList
        fields = '__all__'
        # depth=1