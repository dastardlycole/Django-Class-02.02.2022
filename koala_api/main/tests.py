from django.test import TestCase
from .models import Song
from django.contrib.auth.hashers import check_password

# Create your tests here.


class UserModelTestcase(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        Song.objects.create(title="Take my breath", artist= "The weeknd",publish_date="2022-01-26T10:33:45.239782Z")
        Song.objects.create(title="Take my breath2", artist= "The weeknd2",publish_date="2022-01-26T10:33:45.239782Z")

    def test_single_user(self):
        song = Song.objects.get(id=1)
        # print(hashed_password)
        self.assertEqual(song.title, "Take my breath")
        self.assertEqual(song.artist, "The weeknd")
    
    def test_all_user(self):
        songs = Song.objects.all()
        self.assertEqual(songs.count(), 2)
        
   