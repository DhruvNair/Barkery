from django import forms
from .models import *
from django.utils import timezone

choices=(('Accessory&Clothing','Accessory&Clothing'),
        ('Food Items','Food Items'),
        ('Toys','Toys'),
        ('Medicines','Medicines'),
        ('Animal Furniture','Animal Furniture'),
)
animal_choices = (('Dog','Dog'),
        ('Cat','Cat'),
        ('Rabbit','Rabbit'),
        ('Guinea Pig','Guinea Pig'),
        ('Hamster','Hamster'),
        ('Turtle','Turtle'),
        ('Parrot','Parrot'),
        ('Lizard','Lizard'),
        ('Fish','Fish'),
)

class AddAnimal(forms.ModelForm):
    class Meta:
        model = animal
        fields = ("animal_type","animal_breed","avglife","height","weight","color","temperament")

class AddItem(forms.Form):
    name = forms.CharField(required=True, min_length=3, label='Name of Item')
    type = forms.ChoiceField(choices=choices, label='Type of Item')
    description = forms.CharField(required=True, min_length=3, label='Description')
    cost = forms.FloatField(label='Cost of Item')
    rating = forms.FloatField(label='Rating')
    brand = forms.CharField(required=True, min_length=3, label='Brand')
    animal_types = forms.CharField(required=True, min_length=3,label='For Animal')
    animal_breeds = forms.CharField(required=True, min_length=3, label='And Breed')

class AddLocation(forms.ModelForm):
        class Meta:
                model = location
                fields = ("housenumber","street","pincode","city","state","country")