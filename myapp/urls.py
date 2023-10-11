
from django.contrib import admin
from django.urls import path, re_path
from myapp.models import *
from .views import *

urlpatterns = [
    # открывает главную страницу
    re_path(r'^$', tasks, name='tasks'),
    # открывает страницу для добавления записей
    re_path(r'^add', add_tasks, name='add_tasks')
]
