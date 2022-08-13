from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import ListView
from .models import *


def hotel(request):
     rows = Country.objects.all()
     country_name = {
          'title': rows}
     return render(request, 'my_hotel/hotels.html', country_name)


def cityTurkey(request):
     city_turkey = City.objects.filter(country_id=1)
     city_name = {
          'title': city_turkey}
     return render(request, 'my_hotel/city.html', city_name)

def cityTurkey_Alania(request):
     rows = Hotels.objects.filter(city_id=1)
     hotels = {
          'title': rows,
          'content':rows,
          'photo':rows,
          'free_places':rows}
     return render(request, 'my_hotel/СityTurkey_Alania.html',hotels)

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
