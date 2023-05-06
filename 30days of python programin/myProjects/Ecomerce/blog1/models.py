from django.db import models

# Create your models here.

class collection(models.Model):
    dressname = models.CharField(max_length=30)
    price = models.IntegerField()
    image = models.ImageField(upload_to='option-img/', null=True)
    info = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.dressname
    
class electronics(models.Model):
    machinename = models.CharField(max_length=30)
    price = models.IntegerField()
    image = models.ImageField(upload_to='items-img',null=True)

    def __str__(self):
        return self.machinename
    

#this section is for the individual precised blogs
    