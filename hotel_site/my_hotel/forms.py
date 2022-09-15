from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
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


class ContactForm(forms.ModelForm):
    # hotel = forms.CharField(label='Отель', widget=forms.TextInput(attrs={'placeholder': 'Отель в который летишь'}))
    name_user_ticket = forms.CharField(label='Имя',required=False, widget=forms.TextInput(attrs={'placeholder': 'Ваше имя', 'class': 'form-control datetimepicker-input'}))
    email_user_ticket = forms.EmailField(label='Email', required=False,widget=forms.EmailInput(attrs={'placeholder': 'E-mail', 'class': 'form-control datetimepicker-input'}))
    time_go = forms.DateField(label='Дата Вылета',required=False, widget=forms.DateInput(attrs={'class': 'form-control datetimepicker-input', 'type': 'date'}))
    time_back = forms.DateField(label='Дата Прилета', required=False,widget=forms.DateInput(attrs={'class': 'form-control datetimepicker-input', 'type': 'date'}))

    class Meta:
        model = Ticket
        fields = '__all__'


class EmailSupport(forms.Form):
    subject = forms.CharField(label='Тема', widget=forms.TextInput(attrs={'class': 'form-input'}))
    content = forms.CharField(label='Текст сообщения', widget=forms.Textarea(attrs={'class': 'form-input',
                                                                                    'rows': 5}))


class LoginForm:
    pass
