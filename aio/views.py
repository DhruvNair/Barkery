from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.utils import *
from django.utils.timezone import utc
from django.contrib import messages

def display_home(request):
    return render(request, 'aio/home.html')

#def add_animal(request):



# Create your views here.
