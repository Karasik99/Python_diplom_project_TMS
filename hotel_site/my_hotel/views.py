from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import ListView


def home_page(request):
     return render(request, 'hotel/index.html')

