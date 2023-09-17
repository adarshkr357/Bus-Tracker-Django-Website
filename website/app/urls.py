from django.urls import path
from app import views

urlpatterns = [
    path('', views.index),
    path('base/', views.base),
    path('login/', views.user_login),
    path('register/', views.register),
    path('index/', views.index),
]
