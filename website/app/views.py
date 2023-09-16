from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    return render(request, 'index.html')


def login(request):
    userEmail = request.POST['userEmail']
    userPassword = request.POST['password']
    remember_me = request.POST['remember_me']
    user = authenticate(request, username = userEmail, password = userPassword)
    if user is not None:
        messages.success(request, f'Welcome {userEmail} !!')
        return redirect('/index')
    else:
        messages.error(request, "Invalid Credentials !!")

    return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        messages.success(request, "Profile details updated.")
    return render(request, 'register.html')


def base(request):
    return render(request, 'base.html')

