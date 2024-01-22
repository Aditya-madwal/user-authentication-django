from django.db import models

# Create your models here.

class register(models.Model) :
    username = models.CharField(max_length=50, unique = True)
    name = models.CharField(max_length = 100,blank=True, null=True)
    password = models.CharField(max_length=12)

    def __str__(self):
        return self.username
