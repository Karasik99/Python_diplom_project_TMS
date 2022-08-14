from django.http import request

from . import views
from django.urls import path
from .models import *
urlpatterns = [
    path('', views.prewiew),
    path('Home', views.prewiew),
    path('Choose_countries', views.countries),
    path('hotels.Турция', views.show_cities_Turkey),
    path('hotels.Украина', views.show_cities_Ukraine),
    path('hotels.Египет', views.show_cities_Egipt),
    path('city.<int:id>', views.show_hotels),
    path('hotel.<int:id>', views.show_post),
    path('Attraction', views.attraction),
    path('Restorans', views.restorans),


]
