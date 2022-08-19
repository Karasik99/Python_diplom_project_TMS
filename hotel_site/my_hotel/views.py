from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import ListView
from .models import *
from .forms import LoginForm, UserRegistrationForm

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


def show_hotels(request,id):
     rows = Hotels.objects.filter(city_id=id)
     hotels = {
          'title': rows,
          'content':rows,
          'photo':rows,
          'free_places':rows,
          'id_hotels': rows,
     }
     return render(request, 'my_hotel/test_filter.html', hotels)


def show_post(request,id):
     rows = Hotels.objects.filter(id=id)
     titlews= City.objects.filter(country_id=id)
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
     return render(request, 'my_hotel/show_post.html',context,)



def login(request):
     return render(request, 'my_hotel/auth/login.html')

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            # new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'my_hotel/preview.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'my_hotel/auth/register.html', {'user_form': user_form})




def get_obejct_or_404(Hotels, pk):
     pass

