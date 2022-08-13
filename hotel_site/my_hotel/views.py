from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import ListView
from .models import *


def hotel(request):
     rows = Country.objects.all()
     context = {
          'title': rows}
     return render(request, 'my_hotel/hotels.html', context)


def cityTurkey(request):
     city_turkey = City.objects.filter(country_id=1)
     context = {
          'title': city_turkey}
     return render(request, 'my_hotel/city.html', context)

def cityTurkey_Alania(request):
     return render(request, 'my_hotel/preview.html')

def prewiew(request):
     return render(request, 'my_hotel/preview.html')





def restorans(request):
     pass

def attraction(request):
     pass
# class CountryView(ListView):
#     model = Country
#     template_name = 'my_hotel/hotels.html'
#
#     def country(self):
#      return Country.objects.all()
