from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def sign_up_by_django(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Обработка данных формы
            username = request.POST.get('name')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            age = request.POST.get('age')
            return HttpResponse(f'Добро пожаловать, {username}')
            form.save()
    else:
        form = UserRegistrationForm()
    return render(request, 'fifth_task/registration_page.html', {'form': form})

users = ['nik', 'bob', 'djack']

def sign_up_by_html(request):

    if request.method == 'POST':
        # Получаем данные от пользователя
        username = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        print(f"Имя: {username}")
        print(f"Почтовый адрес: {email}")
        print(f"Возраст: {age}")
        print(f"password1: {password1}")
        print(f"password2: {password2}")

        # проверка на совпадение паролей
        if password1 != password2:
            # Http ответ пользователю
            return HttpResponse('Пароли не совпадают! Заполните форму повторно')
        else:
            # проверка на совпадение login пользователей
            for i in users:
                if i == username:
                    return HttpResponse('Пользователь с таким login уже существует!')
        return HttpResponse(f'Успешная регистрация! Приветствуем, {username}')

        # Если это запрос Get
    return render(request, 'fifth_task/registration_page.html')

