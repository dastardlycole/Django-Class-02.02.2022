from django.db import models
from django.contrib.auth import get_user_model
from django.forms import model_to_dict

User = get_user_model()
# Create your models here.


class Song(models.Model):
    GENRES = (
        ("pop", "POP"),
        ("blues", "Blues"),
        ("rap", "Rap"),
        ("afro_beat", "Afro beat"),
        ("gospel", "Gospel")
    )
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    genre = models.CharField(max_length=355, choices=GENRES, default='pop')
    date_added = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return f"{self.title} by {self.artist}"
    
    
    

class PlayList(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="playlists")
    song       = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="playlists")
    date_added = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return self.user
    
    @property
    def song_detail(self):
        return model_to_dict(self.song)