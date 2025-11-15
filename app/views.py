# app\views.py

from django.shortcuts import render
from django.http import HttpResponse


def app_home(request):
    return HttpResponse('Aqui é o app')
 
def appadd(request):
    return HttpResponse('aqui é o appadd')