from django.db import models

# Create your models here.
class cleint(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=15)
    text = models.CharField(max_length=450)

