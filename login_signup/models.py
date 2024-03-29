from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class task(models.Model) :
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.author} --> {self.title}"
    