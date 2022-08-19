from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.views.generic import ListView
from .models import *
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import login, logout


def preview(request):
     return render(request, 'my_hotel/preview.html')


def countries(request):
     rows = Country.objects.all()
     country_name = {'title': rows}
     return render(request, 'my_hotel/choosecountry.html', country_name)


def show_cities_Turkey(request):
     city_turkey = City.objects.filter(country_id=1)
     city_name = {'title': city_turkey}
     return render(request, 'my_hotel/choosecity.html', city_name)


def show_cities_Ukraine(request):
     city_ukraine = City.objects.filter(country_id=2)
     city_name = {'title': city_ukraine}
     return render(request, 'my_hotel/choosecity.html', city_name)


def show_cities_Egipt(request):
     city_egipt = City.objects.filter(country_id=3)
     city_name = {'title': city_egipt}
     return render(request, 'my_hotel/choosecity.html', city_name)


def show_hotels(request):
    rows = Hotels.objects.all()
    cd = Country.objects.all()
    hotels = {
        'rows':rows,
        'cd':cd,
    }
    return render(request, 'my_hotel/test_filter.html', hotels)


def show_post(request,id):
     rows = Hotels.objects.filter(id=id)
     tags = Hotels.tags.through.objects.filter(hotels_id=id)
     context = {
          'title': rows,
          'content':rows,
          'photo':rows,
          'free_places':rows,
          'id_hotels': rows,
          'tags': tags,
     }
     # {%for tag in tags%}
     #      {{tag.tag}}
     #  {%endfor%}
     return render(request, 'my_hotel/show_post.html',context)


def end(request,id):
    rows = Hotels.objects.filter(id=id)
    context ={'title': rows,
              'content':rows,
              'photo':rows,
              'free_places':rows,
              'id_hotels': rows,
              }
    return render(request, 'my_hotel/forma.html',context)


def user_login(request):
    if request.method == 'POST':
        user_form = UserLoginForm(data=request.POST)
        if user_form.is_valid():
            new_user = user_form.get_user()
            login(request,new_user)
            return redirect('Home')

    else:
        user_form = UserLoginForm()
    return render(request,'my_hotel/auth/login.html', {'user_form': user_form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save()
            login(request, new_user)
            Users.objects.create(name_user = new_user.username,
                                 email_user = new_user.email)

            return render(request, 'my_hotel/preview.html', {'user_form': user_form})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'my_hotel/auth/register.html', {'user_form': user_form})


def user_logout(request):
    logout(request)
    return redirect("Login")


def get_obejct_or_404(Hotels, pk):
     pass

