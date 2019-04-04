from django import forms
from .models import *
from django.utils import timezone

class AddAnimal(forms.ModelForm):
    class Meta:
        model = animal
        fields = ("type","breed","avglife","height","weight","color","temperament")