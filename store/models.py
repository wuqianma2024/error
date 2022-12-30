from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    user=models.OneTooneField(user,null=True,blank=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True)
    email = models.charField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.FloatField()
    digital = models.BooleanField(Default=False,null=True,blank=True)

    def __str__(self):
        return str(self.id)
        