from django.urls import path
"""Определяет схемы URL для blogs."""

from .views import *

app_name = 'blogs'


urlpatterns = [
    path('', index, name='home'),
    path('new_entry/', new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', edit_entry, name='edit_entry'),

]
