from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

#### Pet Adoption tables ####
class animal(models.Model):
    type=models.CharField(max_length=100)
    breed=models.CharField(max_length=100)
    avglife=models.IntegerField(default=0)
    height=models.FloatField(default=0.0)
    weight=models.FloatField(default=0.0)
    color=models.CharField(max_length=100, null=True)
    temperament=models.CharField(max_length=100, null=True)
    class Meta:
        unique_together = (('type', 'breed'))

class location(models.Model):
    housenumber = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    pincode = models.IntegerField(default=0)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    class Meta:
        unique_together = (('pincode', 'street'))

class pet(models.Model):
    animal = models.ForeignKey(animal, on_delete=models.CASCADE)
    name = models.CharField(default= "Tommy", max_length=20)
    age = models.IntegerField(default=0)
    gender = models.BooleanField(default=False)
    remarks = models.CharField(max_length=100)
    daysonbarkery = models.IntegerField(default=0)
    location = models.ForeignKey(location, on_delete=models.CASCADE)
    disease=models.CharField(max_length=100, null=True)

#### Shop tables ####
class brand(models.Model):
    name=models.CharField(default = "Brand", max_length=100, primary_key = True)
    rating=models.FloatField(default=0.0)
    email=models.CharField(max_length=100)
    contact=models.CharField(max_length=10)
    location = models.ForeignKey(location, on_delete=models.CASCADE)

class item(models.Model):
    name = models.CharField(max_length=100)
    animal = models.ForeignKey(animal, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    cost = models.FloatField(default=0.0)
    rating = models.FloatField(default=0.0)
    brand = models.ForeignKey(brand, on_delete=models.CASCADE)