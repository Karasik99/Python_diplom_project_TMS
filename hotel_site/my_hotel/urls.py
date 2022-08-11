from django.http import request

from . import views
from django.urls import path

urlpatterns = [
    path('Hotels', views.hotel),
    path('Restorans', views.restorans),
    path('Attraction', views.attraction),
    path('', views.prewiew),

]
