from django.urls import path
from django.conf.urls import url
#from .views import *
from . import views

urlpatterns = [
	path('', views.display_home, name='home'),
	path('addanimal/',views.add_animal, name='add')
]