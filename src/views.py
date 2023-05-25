import sentry_sdk
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Book
from allauth.socialaccount.models import SocialAccount


def some_view(request):
    # Получение объекта SocialAccount текущего пользователя
    social_account = SocialAccount.objects.get(user=request.user, provider='google')
    # Получение информации о пользователе
    user_info = {
        'name': social_account.extra_data['name'],
        'email': social_account.extra_data['email'],
        'first_name': social_account.extra_data['given_name'],
        'last_name': social_account.extra_data['family_name'],
        'avatar_url': social_account.extra_data['picture'],
    }
    return render(request, 'src/profile.html', {'user_info': user_info})


def main(request):
    return render(request, 'src/Googlelink.html')


def my_view(request):
    try:
        raise ValueError('Пример исключения')
    except Exception as e:
        sentry_sdk.capture_exception(e)
