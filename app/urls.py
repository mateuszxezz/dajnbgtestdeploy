# app\urls.py

from django.urls import path
from . import views 

urlpatterns = [
    path('', views.app_home),
    path('add/', views.appadd)
]