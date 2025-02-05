from django.db import models

class Buyer(models.Model):
    '''Модель представляющая покупателя'''
    name = models.CharField('Имя', max_length=100)
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


class User(models.Model):
    '''Модель представляющая пользователи'''
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class News(models.Model):
    '''Модель представляющая новости'''
    title = models.CharField('Заголовок', max_length=100)
    content = models.TextField('Описание новости')
    data = models.DateTimeField('Дата создания', auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='newses', null=True)

    def __str__(self):
        return self.title

class Novelty(models.Model):
    '''Модель представляющая новинки'''
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='novelties', null=True)

    def __str__(self):
        return self.title