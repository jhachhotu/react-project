from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class PlayerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    age = models.IntegerField()
    team = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True)

class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
