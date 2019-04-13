from django.contrib.auth.models import User
from .models import *
import django_filters

class PetFilter(django_filters.FilterSet):
    class Meta:
        model = pet
        fields = ['pet_name', 'age', 'gender','remarks','color','spayneuter','coatlength',]