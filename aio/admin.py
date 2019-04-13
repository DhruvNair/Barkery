from django.contrib import admin
from .models import animal,pet,location,brand,item,shelter,Profile,vet,pindata,pictures,adoptiondetails

@admin.register(animal,pet,location,brand,item,shelter,Profile,vet,pindata,pictures,adoptiondetails)
class ViewAdmin(admin.ModelAdmin):
	pass