from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.utils import *
from django.utils.timezone import utc
from django.contrib import messages
from django.db import connection
from collections import namedtuple
from .forms import *

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
            type=form.cleaned_data['type']
            breed=form.cleaned_data['breed']
            avglife=form.cleaned_data['avglife']
            height=form.cleaned_data['height']
            weight=form.cleaned_data['weight']
            color=form.cleaned_data['color']
            temperament=form.cleaned_data['temparament']
            try:
                sql_insert_query = """INSERT INTO `animal`
                         VALUES (%s,%s,%d,%f,%f,%s,%s)"""
                cursor = connection.cursor()
                insert_tuple=(type,breed,avglife,height,weight,color,temperament)

                result  = cursor.execute(sql_insert_query,insert_tuple)
                connection.commit()
                print ("Record inserted successfully into python_users table")
                messages.success(request, f'Stock successfully added.')
                return redirect('home')
            except mysql.connector.Error as error :
                connection.rollback() #rollback if any exception occured
                print("Failed inserting record into python_users table {}".format(error))
    context = {
		"form" : form
	 }
    return render(request, "aio/add_animal.html", context)





# Create your views here.
