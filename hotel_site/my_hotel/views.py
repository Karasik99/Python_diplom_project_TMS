from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import ListView


def restorans(request):
     pass

def attraction(request):
     pass

def hotel(request):
     return render(request, 'my_hotel/hotels.html')


def prewiew(request):
     return render(request, 'my_hotel/preview.html')
