from django.http import request

from . import views
from django.urls import path
from .models import *

urlpatterns = [
    path('', views.preview, name='Home'),
    path('Home', views.preview, name='Home'),
    path('Login', views.user_login, name='Login'),
    path('Logout', views.user_logout, name='Out'),
    path('Register', views.register),
    path('hotels', views.show_hotels),
    path('hotel.<int:id>', views.show_post),
    path('booking.<int:id>', views.bookinghotels),
    path('last.<int:id1>.<int:id2>', views.last),
    path('pay/<int:id1>/<int:id2>', views.pdf,name='pay'),
    path('download/<int:id1>/<int:id2>', views.download,name='pay'),




]
