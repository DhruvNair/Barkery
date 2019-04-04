from django.contrib import admin
from .models import *

@admin.register(animal,breed,color,temperament,pet,location,brand,item)
class ViewAdmin(admin.ModelAdmin):
	pass