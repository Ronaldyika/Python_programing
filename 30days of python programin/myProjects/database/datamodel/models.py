from django.db import models

# Create your models here.
class Detailinfo(models.Model):
    name = models.CharField(max_length=30)
    school = models.CharField(max_length=20)
    department = models.CharField(max_length=30)
    subjects = models.CharField(max_length=20)

    def __str__(self):
        return self.name