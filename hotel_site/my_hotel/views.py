from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.views.generic import ListView
from .models import *
from .forms import UserRegistrationForm, UserLoginForm, ContactForm
from django.contrib.auth import login, logout
from django.views.generic import ListView
from django.core.paginator import Paginator
import json



def preview(request):
     return render(request, 'my_hotel/preview.html')


def show_hotels(request):
    rows = Hotels.objects.all()
    country = Country.objects.all()
    city = City.objects.all()
    tags = Tag.objects.all()
    name = Hotels.tags.through.objects.all()
    x = {
        'rows':rows,
        'countries': country,
        'cities': city,
        'tags': tags,
        'name': name,
    }

    return render(request, 'my_hotel/test_filter.html', x)


def show_post(request,id):
     rows = Hotels.objects.filter(id=id)
     tags = Hotels.tags.through.objects.filter(hotels_id=id)
     context = {
          'title': rows,
          'price_econom': rows,
          'price_standart': rows,
          'price_business': rows,
          'content':rows,
          'photo': rows,
          'free_places': rows,
          'id_hotels': rows,
          'tags': tags,
     }
     return render(request, 'my_hotel/show_post.html',context)


def bookinghotels(request,id):
    submitbutton= request.POST.get("submit")
    firstname=''
    emailvalue=''
    date_start=''
    data_end=''
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            ticket = form.save()
            Ticket.objects.create(name_user = ticket.first_name,
                                  email_user = ticket.email,
                                  time_go = ticket.date_start,
                                  time_back=ticket.data_end)
            return render(request, 'my_hotel/preview.html', {'form': form})


            # firstname= form.cleaned_data.get("first_name")
            # emailvalue= form.cleaned_data.get("email")
            # date_start = form.cleaned_data.get("date_start")
            # data_end = form.cleaned_data.get("dataend")
            # context= {'form': form,
            #           'firstname': firstname,
            #           'submitbutton': submitbutton,
            #           'emailvalue':emailvalue,
            #           'date_start': date_start,
            #           'data_end': data_end,
            #           }
            # return render(request, 'my_hotel/preview.html', context)
        else:
            form= ContactForm(request.POST)
            return render(request,'my_hotel/preview.html', {'form': form,
                          'firstname': firstname,
                          'submitbutton': submitbutton,
                          'emailvalue':emailvalue,
                          'date_start': date_start,
                          'data_end': data_end,
                          })
    else:
        form= ContactForm()
        return render(request,'my_hotel/new_forma.html', {'form': form,
                      'firstname': firstname,
                      'submitbutton': submitbutton,
                      'emailvalue':emailvalue,
                      'date_start': date_start,
                      'data_end': data_end,
                      })

    # rows = Hotels.objects.filter(id=id)
    # data = {
    #     'title': rows,
    #     'price_econom': rows,
    #     'price_standart': rows,
    #     'price_business': rows,
    #     'content':rows,
    #     'photo':rows,
    #     'free_places':rows,
    #     'id_hotels': rows,
    #           }
    # if request.user.is_authenticated:
    #     form = ContactForm(data=request.POST)
    #     return render(request, 'my_hotel/new_forma.html',{'form': form})
    # else:
    #     user_form = UserLoginForm()
    #     return render(request,'my_hotel/auth/login.html',{'user_form': user_form})


def pay(request,id):
    return render(request, 'my_hotel/new_hotels-test.html',)


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
