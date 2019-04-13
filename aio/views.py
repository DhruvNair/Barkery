from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import animal
from django.utils.timezone import utc
from django.utils import timezone
from django.contrib import messages
from django.db import connection
from collections import namedtuple
from .forms import *
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from django.utils import timezone
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


def display_home(request):
    #reviews,No. of adopted, no. of strays, No. of shelters, No. of vets,
    #adoptedset=adoptiondetails.objects.filter(adopted=True).order_by(-'dateofadoption')
    return render(request, 'aio/index.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created. You are now able to log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'aio/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        a_form = AddLocation(request.POST)
        if u_form.is_valid() and p_form.is_valid() and a_form.is_valid():
            u_form.save()
            p_form.save()
            housenumber = str(a_form.cleaned_data['housenumber'])
            street = str(a_form.cleaned_data['street'])
            pincode = str(a_form.cleaned_data['pincode'])
            try:
                cursor = connection.cursor()
                cursor.execute(
                    'SELECT * FROM aio_pindata WHERE pincode = %s', [pincode])
                result = dictfetchall(cursor)
                print(result)
                if result == []:
                    messages.error(
                        request, f'Pincode not available in our database')
                    return redirect('profile')
                cursor.execute('CALL newLocation("{}","{}","{}")'.format(
                    housenumber, street, pincode))
                connection.commit()
                print("Record inserted successfully into aio_location table")
                messages.success(request, f'Location successfully added.')
                return redirect('home')
            except mysql.connector.Error as error:
                connection.rollback()  # rollback if any exception occured
                print("Failed inserting record into aio_animals table {}".format(error))
            messages.success(request, f'Your account has been updated.')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        a_form = AddLocation()

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'a_form': a_form,
    }
    return render(request, 'aio/profile.html', context)


def namedtuplefetchall(cursor):
    row = 0
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


def dictfetchall(cursor):
    row = 0
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
            animal_type = str(form.cleaned_data['animal_type'])
            animal_breed = str(form.cleaned_data['animal_breed'])
            avglife = int(form.cleaned_data['avglife'])
            color = str(form.cleaned_data['color'])
            temperament = str(form.cleaned_data['temperament'])
            try:
                cursor = connection.cursor()
                cursor.execute('INSERT INTO `aio_animal` (`animal_type`,`animal_breed`,`avglife`,`color`,`temperament`) VALUES ("{}","{}",{},{},{},"{}","{}");'.format(
                    animal_type, animal_breed, avglife, color, temperament))
                connection.commit()
                print("Record inserted successfully into aio_animals table")
                messages.success(request, f'Stock successfully added.')
                return redirect('home')
            except mysql.connector.Error as error:
                connection.rollback()  # rollback if any exception occured
                print("Failed inserting record into aio_animals table {}".format(error))
    context = {
        "form": form
    }
    return render(request, "aio/add_item.html", context)


def add_item(request):
    form = AddItem()
    if request.method == 'POST':
        form = AddItem(request.POST)
        if form.is_valid():
            item_name = str(form.cleaned_data['name'])
            item_type = str(form.cleaned_data['type'])
            description = str(form.cleaned_data['description'])
            cost = float(form.cleaned_data['cost'])
            rating = float(form.cleaned_data['rating'])
            brand = str(form.cleaned_data['brand'])
            animal_types = str(form.cleaned_data['animal_types'])
            animal_breeds = str(form.cleaned_data['animal_breeds'])
            try:
                cursor = connection.cursor()
                cursor.execute(
                    'SELECT * FROM aio_animal WHERE animal_type = %s AND animal_breed = %s', [animal_types, animal_breeds])
                result = dictfetchall(cursor)
                animalid = result[0]['id']
                cursor.execute(
                    'SELECT * FROM aio_brand WHERE brand_name = %s', [brand])
                result1 = dictfetchall(cursor)
                brandid = result1[0]['brand_name']
                cursor.execute('INSERT INTO `aio_item` (`item_name`,`item_type`,`description`,`cost`,`rating`,`animal_id`,`brand_id`) VALUES ("{}","{}","{}",{},{},{},"{}");'.format(
                    item_name, item_type, description, cost, rating, animalid, brandid))
                connection.commit()
                print("Record inserted successfully into aio_items table")
                messages.success(request, f'Stock successfully added.')
                return redirect('home')
            except mysql.connector.Error as error:
                connection.rollback()  # rollback if any exception occured
                print("Failed inserting record into aio_items table {}".format(error))
    context = {
        "form": form
    }
    return render(request, "aio/add_item.html", context)


def add_location(request):
    form = AddLocation()
    if request.method == 'POST':
        form = AddLocation(request.POST)
        if form.is_valid():
            housenumber = str(form.cleaned_data['housenumber'])
            street = str(form.cleaned_data['street'])
            pincode = str(form.cleaned_data['pincode'])
            try:
                cursor = connection.cursor()
                cursor.execute(
                    'SELECT * FROM aio_pindata WHERE pincode = %s', [pincode])
                result = dictfetchall(cursor)
                print(result)
                if result == []:
                    messages.error(
                        request, f'Pincode not available in our database')
                    return redirect('addlocation')
                cursor.execute('CALL newLocation("{}","{}","{}")'.format(
                    housenumber, street, pincode))
                connection.commit()
                print("Record inserted successfully into aio_location table")
                messages.success(request, f'Location successfully added.')
                return redirect('home')
            except mysql.connector.Error as error:
                connection.rollback()  # rollback if any exception occured
                print("Failed inserting record into aio_animals table {}".format(error))
    context = {
        "form": form
    }
    return render(request, "aio/add_location.html", context)


def add_pet(request):
    form = AddPet()
    form1 = AddLocation()
    if request.method == 'POST':
        form = AddPet(request.POST)
        form1 = AddLocation(request.POST)
        if form.is_valid() and form1.is_valid():
            pet_name = str(form.cleaned_data['pet_name'])
            age = int(form.cleaned_data['age'])
            gender = str(form.cleaned_data['gender'])
            remarks = str(form.cleaned_data['remarks'])
            disease = str(form.cleaned_data['disease'])
            animal_types = str(form.cleaned_data['animal_types'])
            animal_breeds = str(form.cleaned_data['animal_breeds'])
            height = float(form.cleaned_data['height'])
            weight = float(form.cleaned_data['weight'])

            housenumber = str(form1.cleaned_data['housenumber'])
            street = str(form1.cleaned_data['street'])
            pincode = str(form1.cleaned_data['pincode'])
            city = str(form1.cleaned_data['city'])
            location_state = str(form1.cleaned_data['state'])
            country = str(form1.cleaned_data['country'])

            try:
                cursor = connection.cursor()
                cursor.execute(
                    'SELECT * FROM aio_animal WHERE animal_type = %s AND animal_breed = %s', [animal_types, animal_breeds])
                result = dictfetchall(cursor)
                animalid = result[0]['id']
                cursor.execute(
                    'SELECT * FROM aio_pindata WHERE pincode = %s', [pincode])
                result = dictfetchall(cursor)
                print(result)
                if result == []:
                    messages.error(
                        request, f'Pincode not available in our database')
                    return redirect('addpet')
                cursor.execute(
                    'SELECT * FROM aio_location WHERE pincode_id = %s', [pincode])
                result = dictfetchall(cursor)
                if result == []:
                    cursor.execute('CALL newLocation("{}","{}","{}")'.format(
                        housenumber, street, pincode))
                cursor.execute(
                    'SELECT * FROM aio_location WHERE pincode_id = %s', [pincode])
                result = dictfetchall(cursor)
                locationid = result[0]['id']
                cursor.execute('INSERT INTO `aio_pet` (`pet_name`,`age`,`gender`,`remarks`,`disease`,`animal_id`,`location_id`,`height`,`weight`) VALUES ("{}",{},"{}","{}","{}",{},{},{},{});'.format(
                    pet_name, age, gender, remarks, disease, animalid, locationid, height, weight))
                connection.commit()
                print("Record inserted successfully into aio_pet table")
                messages.success(request, f'Stock successfully added.')
                return redirect('home')
            except mysql.connector.Error as error:
                connection.rollback()  # rollback if any exception occured
                print("Failed inserting record into aio_pet table {}".format(error))
    context = {
        "form": form,
        "form1": form1,
    }
    return render(request, "aio/add_pet.html", context)


# Create your views here.
def add_brand(request):
    form = AddBrand()
    form1 = AddLocation()
    if request.method == 'POST':
        form = AddBrand(request.POST)  # , request.FILES
        form1 = AddLocation(request.POST)
        if form.is_valid() and form1.is_valid():
            housenumber = str(form1.cleaned_data['housenumber'])
            street = str(form1.cleaned_data['street'])
            pincode = str(form1.cleaned_data['pincode'])
            city = str(form1.cleaned_data['city'])
            location_state = str(form1.cleaned_data['state'])
            country = str(form1.cleaned_data['country'])

            brand_name = str(form.cleaned_data['brand_name'])
            rating = str(form.cleaned_data['rating'])
            email = str(form.cleaned_data['email'])
            contact = str(form.cleaned_data['contact'])
            # logo=form.cleaned_data['logo']

            try:
                cursor = connection.cursor()
                cursor.execute(
                    'SELECT * FROM aio_pindata WHERE pincode = %s', [pincode])
                result = dictfetchall(cursor)
                print(result)
                if result == []:
                    messages.error(
                        request, f'Pincode not available in our database')
                    return redirect('addbrand')
                cursor.execute(
                    'SELECT * FROM aio_location WHERE pincode_id = %s', [pincode])
                result = dictfetchall(cursor)
                if result == []:
                    cursor.execute('CALL newLocation("{}","{}","{}")'.format(
                        housenumber, street, pincode))
                cursor.execute(
                    'SELECT * FROM aio_location WHERE pincode_id = %s', [pincode])
                result = dictfetchall(cursor)
                locationid = result[0]['id']
                cursor.execute('INSERT INTO `aio_brand` (`brand_name`,`rating`,`email`,`contact`,`location_id`) VALUES ("{}",{},"{}","{}","{}");'.format(
                    brand_name, rating, email, contact, locationid))
                connection.commit()
                print("Record inserted successfully into aio_brand table")
                messages.success(request, f'Stock successfully added.')
                return redirect('home')
            except mysql.connector.Error as error:
                connection.rollback()  # rollback if any exception occured
                print("Failed inserting record into aio_brand table {}".format(error))
    context = {
        "form": form,
        "form1": form1,
    }
    return render(request, "aio/add_brand.html", context)


def adopt_animal(request):
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT distinct animal_type FROM aio_animal')
        result = dictfetchall(cursor)
        animals = []
        for x in range(len(result)):
            animals.append(result[x]['animal_type'])
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
    context = {"animals": animals}
    return render(request, "aio/adopthome.html", context)


def filter(request, animal_names):
    try:
        cursor = connection.cursor()
        # Need Coat length,
        cursor.execute('SELECT animal.animal_breed as breed,pet_name,age,gender,onbarkerysince as daysonbarkery FROM aio_pet WHERE animal.animal_type = animal_names and adopted = False')
        result = dictfetchall(cursor)
        for x in range(len(result)):
            now = timezone.now
            result[x]['daysonbarkery'] = now-result[x]['daysonbarkery']
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
    context = {"pets": result}
    return render(request, "aio/adopt.html", context)


def shop(request):
    context = {}
    return render(request, "aio/shop.html", context)


def vets(request):
    context = {}
    return render(request, "aio/vets.html", context)


def shelters(request):
    context = {}
    return render(request, "aio/shelters.html", context)


def about(request):
    
    context = {}
    return render(request, "aio/about.html", context)
