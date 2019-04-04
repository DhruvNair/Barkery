from django.contrib import admin
from .models import animal,pet,location,brand,item

@admin.register(animal,pet,location,brand,item)
class ViewAdmin(admin.ModelAdmin):
	pass