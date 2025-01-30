from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import UserRegister
from django.http import JsonResponse
from .models import Buyer, Game, News
from django.core.paginator import Paginator

def func_template(request):
    return render(request, "fourth_task/func_template.html")

class class_template(TemplateView):
    template_name = 'fourth_task/class_template.html'

class template_cart(TemplateView):
    template_name = 'fourth_task/cart.html'

def games(request):
    games_collection = Game.objects.all()  # Получаем все записи из модели Game
    context = {
        'games': games_collection,  # Передаем коллекцию в контекст
    }
    return render(request, 'fourth_task/games.html', context)

class template_platform(TemplateView):
    template_name = 'fourth_task/platform.html'


def register_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        balance = request.POST.get('balance')
        age = request.POST.get('age')

        # Проверка, существует ли пользователь с таким именем
        existing_buyers = Buyer.objects.all()
        for buyer in existing_buyers:
            if buyer.name == name:
                return HttpResponse('Пользователь уже существует')

         # Создание нового пользователя
        new_buyer = Buyer.objects.create(name=name, balance=balance, age=age)
        return HttpResponse(f'Пользователь создан успешно: {new_buyer.name}')
    return render(request, 'fifth_task/registration_page.html')

def news(request):
    news = News.objects.all().order_by('data')
    paginator = Paginator(news, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'News.html', {'news': page_obj})

'''
def register_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        balance = request.POST.get('balance')
        age = request.POST.get('age')

        # Проверка, существует ли пользователь с таким именем
        existing_byers = Buyer.objects.all()
        for buyer in existing_byers:
            if buyer.name == name:
                return JsonResponse({'message': 'Пользователь уже существует'})
        # Создание нового пользователя
        new_buyer = Buyer.objects.create(name=name, balance=balance, age=age)
        return JsonResponse({'message': 'Пользователь создан успешно', 'buyer': new_buyer.name})
    return render(request, 'fifth_task/registration_page.html', )

def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')


        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            return HttpResponse('Пароли не совпадают')
        elif username in users:
            info['error'] = 'Пользователь уже существует'
            return HttpResponse('Пользователь уже существует')
        else:
            info['welcome_message'] = f'Приветствуем, {username}!'  # Приветственное сообщение

        return HttpResponse(f'Приветствуем, {username}!')

    return render(request, 'fifth_task/registration_page.html', context=info)


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return HttpResponse('Пароли не совпадают')
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
                return HttpResponse('Вы должны быть старше 18')
            elif username in users:
                info['error'] = 'Пользователь уже существует'
                return HttpResponse('Пользователь уже существует')
            else:
                info['welcome_message'] = f'Приветствуем, {username}!'

            return HttpResponse(f'Приветствуем, {username}!')
    else:
        form = UserRegister()
        info['message'] = form

    return render(request, 'fifth_task/registration_page.html', info)'''
