from django.db import models

# Create your models here.
class userDetail(models.Model):
    
    email = models.EmailField()
    password = models.CharField(max_length=256, blank=True)