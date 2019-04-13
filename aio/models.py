from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from PIL import Image
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator

#### Pet Adoption tables ####
class animal(models.Model):
    animal_type=models.CharField(max_length=100)
    animal_breed=models.CharField(max_length=100)
    avglife=models.IntegerField(default=0)
    color=models.CharField(max_length=1000, null=True)
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

class pictures(models.Model):
    photo1 = models.ImageField(blank=False, default='default.jpg', upload_to='pics')
    photo2 = models.ImageField(blank=False,default='default.jpg', upload_to='pics')
    photo3 = models.ImageField(blank=False,default='default.jpg', upload_to='pics')
    photo4 = models.ImageField(null=True, blank=True, default='default.jpg', upload_to='pics')
    photo5 = models.ImageField(null=True, blank=True, default='default.jpg', upload_to='pics')
    photo6 = models.ImageField(null=True, blank=True, default='default.jpg', upload_to='pics')
    photo7 = models.ImageField(null=True, blank=True, default='default.jpg', upload_to='pics')
    photo8 = models.ImageField(null=True, blank=True, default='default.jpg', upload_to='pics')
    photo9 = models.ImageField(null=True, blank=True, default='default.jpg', upload_to='pics')
    photo10= models.ImageField(null=True, blank=True, default='default.jpg', upload_to='pics')



#### Profile + Vet ####
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    photo = models.ImageField(null=True, blank=True, default='default.jpg', upload_to='profile_pics')
    address = models.ForeignKey(location, on_delete=models.CASCADE, null=True)
    phone = models.CharField(validators=[MinLengthValidator(10)],max_length=13,blank=False,null=True)
    numberofchildren = models.IntegerField(validators=[MinValueValidator(0)],default=0)
    animalpreferences = models.CharField(max_length = 100,blank=False, null=True)
    def __str__(self):
    		return f'{self.user.username} Profile'

class vet(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    address = models.ForeignKey(location, on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)
    
class adoptiondetails(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    adopted = models.BooleanField(default=False)
    dateofadoption = models.DateField(null=True, default=timezone.now)
    def __str__(self):
        return "User : {0} Adopted : {1} Date of Adoption : {2}".format(self.profile.user.username, self.adopted, self.dateofadoption)



class pet(models.Model):
    animal = models.ForeignKey(animal, on_delete=models.CASCADE)
    pet_name = models.CharField(default= "Tommy", max_length=20)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=10,choices=(('M','Male'),('F','Female')),blank=False)
    remarks = models.CharField(max_length=100, null=True)
    onbarkerysince=models.DateTimeField(default=timezone.now)
    color = models.CharField(max_length=100, blank=False, null=True)
    spayneuter = models.CharField(max_length=10, choices=(('Yes','Yes'),('No','No')), blank=False, null=True)
    coatlength = models.CharField(max_length=10, choices=(('Hairless','Hairless'),('Short','Short'),('Medium','Medium'),('Long','Long'),('Wire','Wire'),('Curly','Curly')), blank=False, null=True)
    disease=models.CharField(max_length=100, null=True)
    user = models.ForeignKey(Profile,null=True, on_delete=models.CASCADE)
    photo = models.ForeignKey(pictures, on_delete=models.DO_NOTHING)
    adopt = models.ForeignKey(adoptiondetails, on_delete=models.DO_NOTHING, null=True)
    comments = models.CharField(max_length = 100, null=True, blank=False)
    height=models.FloatField(default=0.0)
    weight=models.FloatField(default=0.0)

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
    stray = models.IntegerField(default=0, validators = [MinValueValidator(0)])