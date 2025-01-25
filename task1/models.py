from django.db import models

class Buyer(models.Model):
    '''Модель представляющая покупателя'''
    name= models.CharField('Имя', max_length=100)
    balance = models.DecimalField('Баланс', max_digits=10, decimal_places=2)
    age = models.IntegerField('Возраст')


    def __str__(self):
        return self.name

class Game(models.Model):
    '''Модель представляющая игру'''
    title= models.CharField('Название игры', max_length=100)
    cost = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    size = models.DecimalField('Размер файлов игры', max_digits=10, decimal_places=2)
    description = models.TextField('Описание')
    age_limited = models.BooleanField('Ограничение возраста 18+', default=False)
    buyer = models.ManyToManyField( Buyer, related_name='games')

    def __str__(self):
        return self.title