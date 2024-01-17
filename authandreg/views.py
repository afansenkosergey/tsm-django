from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from authandreg.forms import RegistrationForm, UserUpdateForm
from shop.models import Category


def register_page(request):
    """
    Вьюха для отображения страницы регистрации нового пользователя.

    Args:
        request (HttpRequest): Запрос от клиента.

    Returns:
        HttpResponse: Ответ с отображением страницы регистрации и формы.

    """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('authandreg:login')
        else:
            messages.warning(request, 'Form is invalid!')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def login_page(request):
    """
    Вьюха для отображения страницы входа пользователя в систему.

    Args:
        request (HttpRequest): Запрос от клиента.

    Returns:
        HttpResponse: Ответ с отображением страницы входа и формы.

    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('articles:list')
        else:
            messages.warning(request, 'Invalid username or password')
    return render(request, 'registration/login.html')


def logout_page(request):
    """
    Вьюха для выхода пользователя из системы.

    Args:
        request (HttpRequest): Запрос от клиента.

    Returns:
        HttpResponse: Перенаправление на страницу списка статей.

    """
    logout(request)
    return redirect('articles:list')


@login_required
def update_profile(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Ваш профиль успешно обновлен!')
            return redirect('shop:user_profile')

    else:
        user_form = UserUpdateForm(instance=request.user)

    return render(request, 'registration/update_profile.html',
                  {'user_form': user_form, 'categories': categories})
