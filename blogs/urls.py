from django.urls import path, include

"""Определяет схемы URL для blogs."""

from .views import *

app_name = 'blogs'


urlpatterns = [
    path('', index, name='home'),
    path('new_entry/', new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', edit_entry, name='edit_entry'),
    # Включить URL авторизации по умолчанию.
    path('', include('django.contrib.auth.urls')),
    # Страница регистрации.
    path('register/', register, name='register'),
]
