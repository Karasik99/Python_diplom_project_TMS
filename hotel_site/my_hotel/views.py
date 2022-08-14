from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import ListView
from .models import *


def prewiew(request):
     return render(request, 'my_hotel/preview.html')


def countries(request):
     rows = Country.objects.all()
     country_name = {'title': rows}
     return render(request, 'my_hotel/countries.html', country_name)


def show_cities_Turkey(request):
     city_turkey = City.objects.filter(country_id=1)
     city_name = {'title': city_turkey}
     return render(request, 'my_hotel/city.html', city_name)


def show_cities_Ukraine(request):
     city_ukraine = City.objects.filter(country_id=2)
     city_name = {'title': city_ukraine}
     return render(request, 'my_hotel/city.html', city_name)


def show_cities_Egipt(request):
     city_egipt = City.objects.filter(country_id=3)
     city_name = {'title': city_egipt}
     return render(request, 'my_hotel/city.html', city_name)


def show_hotels(request,id):
     rows = Hotels.objects.filter(city_id=id)
     hotels = {
          'title': rows,
          'content':rows,
          'photo':rows,
          'free_places':rows,
          'id_hotels': rows,
     }
     return render(request, 'my_hotel/hotels_Alania.html', hotels)


def show_post(request,id):
     rows = Hotels.objects.filter(id=id)
     context = {
          'title': rows,
          'content':rows,
          'photo':rows,
          'free_places':rows,
          'id_hotels': rows,
     }
     return render(request, 'my_hotel/show_post.html',context)







def get_obejct_or_404(Hotels, pk):
     pass



def restorans(request):
     pass

def attraction(request):
     pass
