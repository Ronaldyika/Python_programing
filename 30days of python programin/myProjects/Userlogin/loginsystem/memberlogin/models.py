from django.db import models

# Create your models here.
class Registeration(models.Model):
    name = models.CharField(max_length=340)
    email = models.EmailField(max_length=349)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name