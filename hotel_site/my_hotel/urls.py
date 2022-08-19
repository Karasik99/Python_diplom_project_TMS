from django.http import request

from . import views
from django.urls import path
from .models import *
urlpatterns = [
    path('', views.prewiew),
    path('Home', views.prewiew),
    path('Choose_countries', views.countries),
    path('country.Турция', views.show_cities_Turkey),
    path('country.Украина', views.show_cities_Ukraine),
    path('country.Египет', views.show_cities_Egipt),
    path('city.<int:id>', views.show_hotels),
    path('hotel.<int:id>', views.show_post),



]
