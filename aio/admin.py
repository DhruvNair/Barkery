from django.contrib import admin
from .models import animal,pet,location,brand,item,shelter,Profile,vet,pindata

@admin.register(animal,pet,location,brand,item,shelter,Profile,vet,pindata)
class ViewAdmin(admin.ModelAdmin):
	pass