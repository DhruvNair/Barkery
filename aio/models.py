from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

#### Pet Adoption tables ####
class breed(models.Model):
    breedname=models.CharField(max_length=100)
    lifespan=models.IntegerField(default=0)
    height=models.FloatField(default=0.0)
    weight=models.FloatField(default=0.0)
class animal(models.Model):
    breedname=models.ForeignKey(breed, on_delete=models.CASCADE)
    typename=models.CharField(max_length=100)


    
class color(models.Model):
    breedname=models.ManyToManyField(breed)
    color=models.CharField(max_length=0)

class temperament(models.Model):
    breedname=models.ManyToManyField(breed)
    temperament=models.CharField(max_length=100)

class pet(models.Model):
    animal = models.ForeignKey(animal, on_delete=models.CASCADE)   
    age = models.IntegerField(default=0)
    gender = models.BooleanField(default=False)
    remarks = models.CharField(max_length=100)
    daysonbarkery = models.IntegerField(default=0)
    location = models.ForeignKey(petlocation, on_delete=models.CASCADE)

class petlocation(models.Model):
    housenumber = models.CharField(max_length=100)
    street = models.charField(max_length=100)
    pincode = models.IntegerField(default=0)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

class disease(models.Model):
    pet=models.ForeignKey(pet, on_delete=models.CASCADE)
    disease=models.CharField(max_length=100)



#### SHop tables ####
class brand:
    brandname=models.CharField(max_length=100)
    brandrating=models.FloatField(default=0.0)
    email=models.CharField(max_length=100)
    contact=models.CHarField(max_length=10)
    
class brandlocation(models.Model):
    brand=models.ForeignKey(brand, on_delete=models.CASCADE)
    housenumber = models.CharField(max_length=100)
    street = models.charField(max_length=100)
    pincode = models.IntegerField(default=0)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

class item:
    itemname = models.CharField(max_length=100)
    animal = models.ForeignKey(animal, on_delete=models.CASCADE)
    itemtype = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    cost = models.FloatField(default=0.0)
    rating = models.FloatField(default=0.0)
    brand = models.ForeignKey(brand, on_delete=models.CASCADE)


# Create your models here.
