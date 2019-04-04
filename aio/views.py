from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import animal
from django.utils import *
from django.utils.timezone import utc
from django.contrib import messages
from django.db import connection
from collections import namedtuple
from .forms import AddAnimal
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

def display_home(request):
    return render(request, 'aio/home.html')



def namedtuplefetchall(cursor):
    row=0
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def add_animal(request):
    form = AddAnimal()
    if request.method == 'POST':
        form = AddAnimal(request.POST)
        if form.is_valid():
            type=str(form.cleaned_data['type'])
            breed=str(form.cleaned_data['breed'])
            avglife=int(form.cleaned_data['avglife'])
            height=float(form.cleaned_data['height'])
            weight=float(form.cleaned_data['weight'])
            color=str(form.cleaned_data['color'])
            temperament=str(form.cleaned_data['temperament'])
            try:
                cursor = connection.cursor()
                cursor.execute('INSERT INTO `aio_animal` (`type`,`breed`,`avglife`,`height`,`weight`,`color`,`temperament`) VALUES ("{}","{}",{},{},{},"{}","{}");'.format(type,breed,avglife,height,weight,color,temperament))
                connection.commit()
                print ("Record inserted successfully into python_users table")
                messages.success(request, f'Stock successfully added.')
                return redirect('home')
            except mysql.connector.Error as error :
                connection.rollback() #rollback if any exception occured
                print("Failed inserting record into aio_animals table {}".format(error))
    context = {
		"form" : form
	 }
    return render(request, "aio/add_animal.html", context)





# Create your views here.
