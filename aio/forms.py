from django import forms
from .models import *
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
choices = (('Accessory&Clothing', 'Accessory&Clothing'),
           ('Food Items', 'Food Items'),
           ('Toys', 'Toys'),
           ('Medicines', 'Medicines'),
           ('Animal Furniture', 'Animal Furniture'),)
animal_choices = (('Dog', 'Dog'),
                  ('Cat', 'Cat'),
                  ('Rabbit', 'Rabbit'),
                  ('Guinea Pig', 'Guinea Pig'),
                  ('Hamster', 'Hamster'),
                  ('Turtle', 'Turtle'),
                  ('Parrot', 'Parrot'),
                  ('Lizard', 'Lizard'),
                  ('Fish', 'Fish'),)
ch = (('M', 'Male'),
      ('F', 'Female'),)

choices12 = (('Hairless', 'Hairless'), ('Short', 'Short'), ('Medium','Medium'), ('Long', 'Long'), ('Wire', 'Wire'), ('Curly', 'Curly'))


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['photo', 'bio', 'phone',
                  'numberofchildren', 'animalpreferences']


class AddAnimal(forms.Form):
    animal_type = forms.ChoiceField(
        choices=animal_choices, label='Type of Animal')
    animal_breed = forms.CharField(
        required=True, min_length=3, strip=True, label='And Breed')
    avglife = forms.IntegerField(min_value=1, label="Average Life")
    color = forms.CharField(required=True, min_length=3,
                            strip=True, label='Colors Available')
    temperament = forms.CharField(
        required=True, min_length=3, strip=True, label='General Temperament')


class AddItem(forms.Form):
    name = forms.CharField(required=True, min_length=3,
                           strip=True, label='Name of Item')
    type = forms.ChoiceField(choices=choices, label='Type of Item')
    description = forms.CharField(
        required=True, min_length=3, strip=True, label='Description')
    cost = forms.FloatField(min_value=1.0, label='Cost of Item')
    rating = forms.FloatField(min_value=1.0, label='Rating')
    brand = forms.CharField(required=True, min_length=3,
                            strip=True, label='Brand')
    animal_types = forms.ChoiceField(
        choices=animal_choices, label='For Animal')
    animal_breeds = forms.CharField(
        required=True, min_length=3, strip=True, label='And Breed')


class AddLocation(forms.Form):
    housenumber = forms.CharField(
        required=True, min_length=2, strip=True, label="House Name")
    street = forms.CharField(required=True, min_length=2,
                             strip=True, label="Street")
    pincode = forms.CharField(
        required=True, min_length=5, max_length=6, strip=True, label="Pincode")


class AddPet(forms.Form):
    pet_name = forms.CharField(
        required=True, min_length=2, strip=True, label="Name of Pet")
    age = forms.IntegerField(min_value=0, label="Age of Pet")
    gender = forms.ChoiceField(choices=ch, label='Gender')
    remarks = forms.CharField(strip=True, label="Remarks(if any)")
    disease = forms.CharField(
        strip=True, label="Diseases(if any): [Separate using ,]")
    animal_types = forms.CharField(
        required=True, min_length=3, strip=True, label='Animal')
    animal_breeds = forms.CharField(
        required=True, min_length=3, strip=True, label='Breed')
    height = forms.FloatField(min_value=0.1, label="Height")
    weight = forms.FloatField(min_value=0.1, label="Weight")
    coatlength = forms.ChoiceField(choices=choices12, label='Coat Length')
    color = forms.CharField(strip=True, required=True,
                            min_length=3, label="Color of the Pet")
    #photo = forms.ImageField()


class AddBrand(forms.ModelForm):
    email = forms.EmailField()
    rating = forms.FloatField(min_value=1.0)
    contact = forms.CharField(
        required=True, strip=True, min_length=10, max_length=13)

    class Meta:
        model = brand
        fields = ['brand_name', 'rating', 'email', 'contact', ]
