from django import forms
from .models import *
from django.utils import timezone

class AddAnimal(forms.ModelForm):
    class Meta:
        model = animal
        fields = ("typename","breedname","lifespan","height","weight","color","temperament")