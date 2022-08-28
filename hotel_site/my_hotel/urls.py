from django.http import request

from . import views
from django.urls import path
from .models import *
urlpatterns = [
    path('', views.preview),
    path('Home', views.preview , name='Home'),
    path('Login', views.user_login, name='Login'),
    path('Logout', views.user_logout, name='Out'),
    path('Register', views.register),
    # path('Choose_countries', views.countries),
    # path('country.Турция', views.show_cities_Turkey),
    # path('country.Украина', views.show_cities_Ukraine),
    # path('country.Египет', views.show_cities_Egipt),
    path('hotels', views.show_hotels),
    path('hotel.<int:id>', views.show_post),
    path('booking', views.bookinghotels),



]
