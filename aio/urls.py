from django.urls import path
from django.conf.urls import url
#from .views import *
from . import views

urlpatterns = [
	path('', views.display_home, name='home'),
	path('addanimal/',views.add_animal, name='addanimal'),
	path('additem/',views.add_item, name='additem'), 
	path('addlocation/',views.add_location, name='addlocation'),
	path('addpet/',views.add_pet, name='addpet'),
]