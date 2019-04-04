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

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def add_animal(request):
    form = AddAnimal()
    if request.method == 'POST':
        form = AddAnimal(request.POST)
        if form.is_valid():
            animal_type=str(form.cleaned_data['animal_type'])
            animal_breed=str(form.cleaned_data['animal_breed'])
            avglife=int(form.cleaned_data['avglife'])
            height=float(form.cleaned_data['height'])
            weight=float(form.cleaned_data['weight'])
            color=str(form.cleaned_data['color'])
            temperament=str(form.cleaned_data['temperament'])
            try:
                cursor = connection.cursor()
                cursor.execute('INSERT INTO `aio_animal` (`animal_type`,`animal_breed`,`avglife`,`height`,`weight`,`color`,`temperament`) VALUES ("{}","{}",{},{},{},"{}","{}");'.format(animal_type,animal_breed,avglife,height,weight,color,temperament))
                connection.commit()
                print ("Record inserted successfully into aio_animals table")
                messages.success(request, f'Stock successfully added.')
                return redirect('home')
            except mysql.connector.Error as error :
                connection.rollback() #rollback if any exception occured
                print("Failed inserting record into aio_animals table {}".format(error))
    context = {
		"form" : form
	 }
    return render(request, "aio/add_animal.html", context)

def add_item(request):
    form = AddItem()
    if request.method == 'POST':
        form = AddItem(request.POST)
        if form.is_valid():
            item_name=str(form.cleaned_data['name'])
            item_type=str(form.cleaned_data['type'])
            description=int(form.cleaned_data['description'])
            cost=float(form.cleaned_data['cost'])
            rating=float(form.cleaned_data['rating'])
            brand=str(form.cleaned_data['brand'])
            animal_types=str(form.cleaned_data['animal_type'])
            animal_breeds=str(form.cleaned_data['animal_breed'])
            try:
                cursor = connection.cursor()
                cursor.execute('SELECT * FROM aio_animal WHERE animal_type = %s AND animal_breed = %s', [animal_type,animal_breed])
                result = dictfetchall(cursor)
                animalid=result[0].id
                cursor.execute('SELECT * FROM aio_brand WHERE brand_name = %s', [brand])
                result1 = dictfetchall(cursor)
                brandid=result[0].id
                cursor.execute('INSERT INTO `aio_item` (`item_name`,`item_type`,`description`,`cost`,`rating`,`animal`,`brand`) VALUES ("{}","{}","{}",{},{},{},{});'.format(item_name,item_type,description,cost,rating))
                connection.commit()
                print ("Record inserted successfully into aio_items table")
                messages.success(request, f'Stock successfully added.')
                return redirect('home')
            except mysql.connector.Error as error :
                connection.rollback() #rollback if any exception occured
                print("Failed inserting record into aio_items table {}".format(error))



# Create your views here.
