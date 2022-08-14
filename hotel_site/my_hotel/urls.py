from django.http import request

from . import views
from django.urls import path
from .models import *
urlpatterns = [
    path('', views.prewiew),
    path('Hotels', views.countries),
    path('hotels.Турция', views.show_cities_Turkey),
    path('Алания', views.show_hotels_Alania),
    path('Attraction', views.attraction),
    path('Restorans', views.restorans),
    path('hotel.<int:id>', views.show_post),


]
