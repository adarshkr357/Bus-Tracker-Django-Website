from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from app.models import *
import random

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    return render(request, 'index.html')


def login(request):
    if request.method == "POST":
        userEmail = request.POST['userData']
        userPassword = request.POST['password']
        if '@' in userEmail:
            user = authenticate(request, email = userEmail, password = userPassword)
        else:
            user = authenticate(request, username = userEmail, password = userPassword)
        if user is not None:
            messages.success(request, f'Welcome {userEmail} !!')
            return redirect('/index')
        else:
            messages.warning(request, "Invalid Credentials !!")

    return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        full_name = request.POST['full_name']
        username = request.POST['username']
        email = request.POST['email'] + "@gmail.com"
        password = request.POST['password']
        uid = random.randint(11111111, 99999999)
        if request.POST['bus_number']:
            busNum = request.POST['bus_number']
            busName = request.POST['bus_name']
            fuel = request.POST['fuel_type']
            routes = request.POST['bus_route']
            fares = request.POST['bus_fare']
            emc = request.POST['emc']
            if emc:
                Driver(
                    bus_num = busNum,
                    bus_name = busName,
                    driver_id = uid,
                    driver_username = username,
                    driver_email = email,
                    driver_password = password,
                    driver_name = full_name,
                    bus_route = routes,
                    fare = fares,
                    fuel_type = fuel,
                    emission_compliance = emc
                ).save
            else:
                Driver(
                    bus_num = busNum,
                    bus_name = busName,
                    driver_id = uid,
                    driver_username = username,
                    driver_email = email,
                    driver_password = password,
                    driver_name = full_name,
                    bus_route = routes,
                    fare = fares,
                    fuel_type = fuel
                ).save
            request.session['user_type'] = "driver"
        else:
            Passenger(
                user_id = uid,
                name = full_name,
                username = username,
                email = email,
                password = password
            ).save
            request.session['user_type'] = "passenger"
        messages.success(request, f"You are registered as {request.session['user_type']}.")
        return redirect('/index')
    return render(request, 'register.html')


def base(request):
    return render(request, 'base.html')

