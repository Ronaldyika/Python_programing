from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class postmodel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    datecreated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-datecreated',)

    def __str__(self):
        return self.title