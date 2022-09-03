from datetime import datetime

from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Ticket


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    # class Meta:
    #     model = User
    #     fields = ['username','password']


class ContactForm(forms.ModelForm):
    # hotel = forms.CharField(label='Отель', widget=forms.TextInput(attrs={'placeholder': 'Отель в который летишь'}))
    name_user_ticket = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'placeholder': 'Ваше имя', 'class': 'form-control datetimepicker-input',}))
    email_user_ticket = forms.EmailField(label='Email' , widget=forms.EmailInput(attrs={'placeholder': 'E-mail', 'class': 'form-control datetimepicker-input'}))
    time_go = forms.DateField(label='Дата Вылета', widget=forms.DateInput(attrs={
                                                                                                               'class': 'form-control datetimepicker-input',

                                                                                                               'type': 'date'}))
    time_back = forms.DateField(label='Дата Прилета',  widget=forms.DateInput(attrs={
                                                                                                               'class': 'form-control datetimepicker-input',

                                                                                                               'type': 'date'}))


    class Meta:
        model = Ticket
        fields = '__all__'
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-input'}),
        #     'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        # }
    # def save(self):
    #     data = self.cleaned_data
    #     name_user_ticket=data['name_user_ticket']
    #     email_user_ticket=data['email_user_ticket']
    #     self.save()



    # class Meta:
    #     model = User
    #     fields = ['username','password']

class LoginForm:
    pass
