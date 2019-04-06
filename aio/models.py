from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    
    def __str__(self):
        return "Animal Type : {0} Breed : {1} Lifespan : {2} Height : {3} Weight : {4}".format(self.animal_type, self.animal_breed, self.avglife, self.height, self.weight)

class pindata(models.Model):
    pincode = models.CharField(max_length = 10, primary_key=True)
    city = models.CharField(max_length = 20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)

    def __str__(self):
        return "Pincode : {0} City : {1} State : {2} Country : {3}".format(self.pincode, self.city, self.state, self.country)

class location(models.Model):
    housenumber = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    pincode = models.ForeignKey(pindata, on_delete=models.CASCADE)

    def __str__(self):
        return "House Number : {0} Street : {1} Pincode : {2}".format(self.housenumber, self.street, self.pincode)


#### Profile + Vet ####
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    photo = models.ImageField(null=True, blank=True)

class vet(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    location = models.ForeignKey(location, on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)

class pet(models.Model):
    animal = models.ForeignKey(animal, on_delete=models.CASCADE)
    pet_name = models.CharField(default= "Tommy", max_length=20)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=10,choices=(('M','Male'),('F','Female')),blank=False)
    remarks = models.CharField(max_length=100, null=True)
    onbarkerysince=models.DateTimeField(default=timezone.now)
    location = models.ForeignKey(location, on_delete=models.CASCADE)
    disease=models.CharField(max_length=100, null=True)
    user = models.ForeignKey(Profile,null=True, on_delete=models.CASCADE)
    photo = models.ImageField(null=True, blank=True, default='default.jpg', upload_to='pet_pics')
    adopted = models.BooleanField(default=False)

    def __str__(self):
        return "Animal Type : {0} Breed : {1} Age : {2} Gender : {3} Adopted : {4}".format(self.animal.animal_type, self.animal.animal_breed, self.age, self.gender, self.adopted)


#### Shop tables ####
class brand(models.Model):
    brand_name=models.CharField(default = "Brand", max_length=100, primary_key = True)
    rating=models.FloatField(default=0.0)
    email=models.CharField(max_length=100, null=True)
    contact=models.CharField(max_length=10, null=True)
    location = models.ForeignKey(location, on_delete=models.CASCADE)
    logo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return "Brand Name : {0} Rating : {1} Email : {2} Contact : {3}".format(self.brand_name, self.rating, self.email, self.contact)


class item(models.Model):
    item_name = models.CharField(max_length=100)
    animal = models.ForeignKey(animal, on_delete=models.CASCADE)
    item_type = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    cost = models.FloatField(default=0.0)
    rating = models.FloatField(default=0.0)
    brand = models.ForeignKey(brand, on_delete=models.CASCADE)
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return "Item Name : {0} Item Type : {1} Animal Type : {2} Cost : {3} Brand : {4}".format(self.item_name, self.item_type, self.animal.animal_type, self.cost, self.brand.brand_name)


class shelter(models.Model):
    shelter_name = models.CharField(max_length=50)
    location = models.ForeignKey(location, on_delete=models.CASCADE)
    animals = models.CharField(max_length=100)
    logo = models.ImageField(null=True, blank=True)