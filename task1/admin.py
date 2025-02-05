from django.contrib import admin
from .models import Game, Buyer, News, User, Novelty

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size')  # Отображение полей
    list_filter = ('size', 'cost')  # Фильтрация по полям
    search_fields = ('title',)  # Поиск по полю title
    list_per_page = 20  # Ограничение кол-ва записей до 20

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age')  # Отображение полей
    list_filter = ('balance', 'age')  # Фильтрация по полям
    search_fields = ('name',)  # Поиск по полю name
    list_per_page = 30  # Ограничение кол-ва записей до 30

    readonly_fields = ('balance',)  # Поле balance только для чтения

@admin.register(News)
class News(admin.ModelAdmin):
    list_display = ('title', 'content', 'data')  # Отображение полей
    list_filter = ('title', 'data')  # Фильтрация по полям
    search_fields = ('title',)  # Поиск по полю name
    list_per_page = 30  # Ограничение кол-ва записей до 30

admin.site.register(User)
admin.site.register(Novelty)