from django.shortcuts import render
from django.http import HttpResponse


def index_home(request):
    return render(request, 'appinfos/index.html')

    