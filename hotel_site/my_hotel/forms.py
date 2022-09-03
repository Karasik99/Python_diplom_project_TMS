from datetime import datetime

from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


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


class ContactForm(forms.Form):
    # hotel = forms.CharField(label='Отель', widget=forms.TextInput(attrs={'placeholder': 'Отель в который летишь'}))
    name_user_ticket = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'placeholder': 'Ваше имя', 'class': 'form-control datetimepicker-input'}))
    email_user_ticket = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'E-mail', 'class': 'form-control datetimepicker-input'}))
    time_go = forms.DateField(label='Дата Вылета', input_formats=['%d/%m/%Y'],widget=forms.DateInput(attrs={
                                                                                                               'class': 'form-control datetimepicker-input',
                                                                                                               'data-target': '#datetimepicker1',
                                                                                                               'type': 'date'}))
    time_back = forms.DateField(label='Дата Прилета', input_formats=['%d/%m/%Y'], widget=forms.DateInput(attrs={
                                                                                                               'class': 'form-control datetimepicker-input',
                                                                                                               'data-target': '#datetimepicker1',
                                                                                                               'type': 'date'}))

    def save(self, *args, **kwargs):
        super(ContactForm, self).save(*args, **kwargs)
    # class Meta:
    #     model = User
    #     fields = ['username','password']

class LoginForm:
    pass
