from django.http import request

from . import views
from django.urls import path

urlpatterns = [
    path('', views.prewiew),
    path('Hotels', views.hotel),
    path('hotels.Турция', views.cityTurkey),
    path('Алания', views.cityTurkey_Alania),
    path('Attraction', views.attraction),
    path('Restorans', views.restorans),


]
