from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h4>Проверка работает<h4>")

def about(request):
    return HttpResponse("<h4>Страница про нас<h4>")

def first(request):
    return HttpResponse("<h4>Первая страница<h4>")

def second(request):
    return HttpResponse("<h4>Следующая страница<h4>")
