
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publish_date = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True)

class Song(models.Model):
    title = models.CharField(max_length=300)
    artist = models.CharField(max_length=300)
    publish_date = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True,blank=True)
    
class Playlist(models.Model):
    user = models.CharField(max_length=300, blank=True, null=True)
    song = models.CharField(max_length=300)
    date_added = models.DateTimeField(auto_now_add=True)    
        