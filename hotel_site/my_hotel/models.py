from django.db import models

from django.urls import reverse


class Country(models.Model):
    title = models.CharField(max_length=255, verbose_name='Страна')

    def __str__(self):
        return self.title


class City(models.Model):
    title = models.CharField(max_length=255, verbose_name='Город')
    country = models.ForeignKey('Country', on_delete=models.PROTECT, verbose_name='Город')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("city", kwargs={"city": self.pk})



class Hotels(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Данные')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фотография')
    is_working = models.BooleanField(default=True, verbose_name='Публикация')
    free_places = models.IntegerField(verbose_name='Кол-во мест')
    price_econom = models.IntegerField(verbose_name='Цена Эконома', default=100)
    price_standart = models.IntegerField(verbose_name='Цена Стандарта', default=150)
    price_business = models.IntegerField(verbose_name='Цена Бизнеса', default=200)
    city = models.ForeignKey('City', on_delete=models.PROTECT, verbose_name='Город')
    tags = models.ManyToManyField('Tag')


    def __str__(self):
        return self.title


class Galery(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',verbose_name='Фотография')
    hotel_id = models.ForeignKey('Hotels', on_delete=models.PROTECT, verbose_name='Город')


class Tag(models.Model):
    tag = models.CharField(max_length=255, verbose_name='Тэг')

    def __str__(self):
        return self.tag


class Users(models.Model):
    name_user = models.CharField(max_length=30, verbose_name='Имя')
    email_user = models.EmailField(max_length=30, verbose_name='Email')


    def __str__(self):
        return self.name_user

class Ticket(models.Model):
    name_user_ticket = models.CharField(max_length=30, verbose_name='Имя')
    email_user_ticket = models.EmailField(max_length=30, verbose_name='Email')
    time_go = models.DateField(verbose_name='Дата вылета',)
    time_back = models.DateField(verbose_name='Дата прилета',)
    CHOOSE = [
        (1, 'Эконом Вариант'),
        (2, 'Стандартный Номер'),
        (3, 'Бизнес люкс'),
    ]
    choose = models.PositiveSmallIntegerField( ("choose"), choices=CHOOSE,blank=False,default=1)
