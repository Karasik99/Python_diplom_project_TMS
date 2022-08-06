from django.http import request

from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_page)
]
