from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

#### Pet Adoption tables ####
class animal(models.Model):
    typename=models.CharField(max_length=100)
    breedname=models.CharField(max_length=100)
    lifespan=models.IntegerField(default=0)
    height=models.FloatField(default=0.0)
    weight=models.FloatField(default=0.0)
    color=models.CharField(max_length=10, null=True)
    temperament=models.CharField(max_length=100, null=True)

class location(models.Model):
    housenumber = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    pincode = models.IntegerField(default=0)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

class pet(models.Model):
    animal = models.ForeignKey(animal, on_delete=models.CASCADE)   
    age = models.IntegerField(default=0)
    gender = models.BooleanField(default=False)
    remarks = models.CharField(max_length=100)
    daysonbarkery = models.IntegerField(default=0)
    location = models.ForeignKey(location, on_delete=models.CASCADE)
    disease=models.CharField(max_length=100, null=True)

#### Shop tables ####
class brand(models.Model):
    brandname=models.CharField(max_length=100)
    brandrating=models.FloatField(default=0.0)
    email=models.CharField(max_length=100)
    contact=models.CharField(max_length=10)
    location = models.ForeignKey(location, on_delete=models.CASCADE)

class item(models.Model):
    itemname = models.CharField(max_length=100)
    animal = models.ForeignKey(animal, on_delete=models.CASCADE)
    itemtype = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    cost = models.FloatField(default=0.0)
    rating = models.FloatField(default=0.0)
    brand = models.ForeignKey(brand, on_delete=models.CASCADE)