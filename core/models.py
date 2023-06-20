from django.db import models
from django.contrib.auth.models import User

class Song(models.Model):
    id = models.AutoField(primary_key=True)
    music=models.FileField(upload_to='song', max_length=100)
    name=models.CharField(max_length=10)

class Favoirite(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    song=models.ForeignKey(Song, on_delete=models.CASCADE)