from django.contrib import admin
from .models import *

@admin.register(animal,breed,color,temperament,pet,petlocation,brand,brandlocation,item)
class ViewAdmin(admin.ModelAdmin):
	pass