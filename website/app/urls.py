from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.index),
    path('base', views.base),
    path('login', views.login),
    path('register', views.register),
]
