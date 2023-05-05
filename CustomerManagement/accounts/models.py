from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200 ,null=True)
    phone = models.CharField(max_length=34 ,null=True)
    email = models.EmailField(max_length=399 ,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('indoor','indoor'),
        ('outdoor','outdoor')
    )
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200,null=True,choices= CATEGORY)
    description = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)


class Order(models.Model):
    STATUS = (
        ('pending','pending'),
        ('out for delivery','out for delivery'),
        ('delivered','delivered')
    )
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    status = models.CharField(max_length=200 ,null=True,choices=STATUS)