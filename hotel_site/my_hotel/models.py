from django.db import models


class Country(models.Model):
    title = models.CharField(max_length=255, verbose_name='Страна')

    def __str__(self):
        return self.title


class City(models.Model):
    title = models.CharField(max_length=255, verbose_name='Город')
    country = models.ForeignKey('Country', on_delete=models.PROTECT, verbose_name='Город')

    def __str__(self):
        return self.title


class Hotels(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Данные')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фотография')
    is_working = models.BooleanField(default=True, verbose_name='Публикация')
    free_places = models.IntegerField(verbose_name='Кол-во мест')
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
