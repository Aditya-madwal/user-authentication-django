from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class register(models.Model) :
    username = models.CharField(max_length=50, unique = True)
    name = models.CharField(max_length = 100,blank=True, null=True)
    password = models.CharField(max_length=12)

    def __str__(self):
        return self.username

class task(models.Model) :
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.author} --> {self.title}"
    