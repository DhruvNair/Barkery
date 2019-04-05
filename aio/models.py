from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

#### Pet Adoption tables ####
class animal(models.Model):
    animal_type=models.CharField(max_length=100)
    animal_breed=models.CharField(max_length=100)
    avglife=models.IntegerField(default=0)
    height=models.FloatField(default=0.0)
    weight=models.FloatField(default=0.0)
    color=models.CharField(max_length=100, null=True)
    temperament=models.CharField(max_length=100, null=True)
    class Meta:
        unique_together = (('animal_type', 'animal_breed'))

class location(models.Model):
    housenumber = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)
    city = models.CharField(max_length=100)
    location_state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

class pet(models.Model):
    animal = models.ForeignKey(animal, on_delete=models.CASCADE)
    pet_name = models.CharField(default= "Tommy", max_length=20)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=10,choices=(('M','Male'),('F','Female')),blank=False)
    remarks = models.CharField(max_length=100, null=True)
    onbarkerysince=models.DateTimeField(default=timezone.now)
    location = models.ForeignKey(location, on_delete=models.CASCADE)
    disease=models.CharField(max_length=100, null=True)
    photo = models.ImageField(null=True)

#### Shop tables ####
class brand(models.Model):
    brand_name=models.CharField(default = "Brand", max_length=100, primary_key = True)
    rating=models.FloatField(default=0.0)
    email=models.CharField(max_length=100, null=True)
    contact=models.CharField(max_length=10, null=True)
    location = models.ForeignKey(location, on_delete=models.CASCADE)
    logo = models.ImageField(null=True)

class item(models.Model):
    item_name = models.CharField(max_length=100)
    animal = models.ForeignKey(animal, on_delete=models.CASCADE)
    item_type = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    cost = models.FloatField(default=0.0)
    rating = models.FloatField(default=0.0)
    brand = models.ForeignKey(brand, on_delete=models.CASCADE)
    photo = models.ImageField(null=True)

class shelter(models.Model):
    shelter_name = models.CharField(max_length=50)
    location = models.ForeignKey(location, on_delete=models.CASCADE)
    animals = models.CharField(max_length=100)
    logo = models.ImageField(null=True)


class vet(models.Model):
    # profile = 
    specialization = models.CharField(max_length=100)
    location = models.ForeignKey(location, on_delete=models.CASCADE)