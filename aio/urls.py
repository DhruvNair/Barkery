from django.urls import path
from django.conf.urls import url
#from .views import *
from . import views

urlpatterns = [
	path('', views.display_home, name='home'),
	path('adopt/',views.adoptionhome,name='adopt'),
	path('adoptfilter/',views.adoptani,name='adoptfilter'),
	path('adoptpage/',views.adoptapet, name='adoptpage'),
	path('adoptdisplay/',views.displayanimals, name='disp'),
	# path('adopt/<slug:animal_names>', views.filter, name='filter'),
	path('shop/', views.shop, name='shop'),
	path('vets/', views.vets, name='vets'),
	path('shelters/', views.shelters, name='shelters'),
	path('about/', views.about, name='aboutus'),
	path('addanimal/',views.add_animal, name='addanimal'),
	path('additem/',views.add_item, name='additem'), 
	path('addlocation/',views.add_location, name='addlocation'),
	path('addpet/',views.add_pet, name='addpet'),
	path('addbrand/', views.add_brand, name='addbrand'),
]