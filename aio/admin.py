from django.contrib import admin
from .models import *

@admin.register(animal,pet,location,brand,item)
class ViewAdmin(admin.ModelAdmin):
	pass