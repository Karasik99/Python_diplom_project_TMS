from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import ListView


def restorans(request):
     pass

def attraction(request):
     pass

def hotel(request):
     pass

def home_page(request):
     return render(request, 'my_hotel/index_test.html')
