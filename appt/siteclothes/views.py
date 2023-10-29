from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Страница приложения siteclothes')


def jeans(request):
    return HttpResponse('Каталог jeans')


def tops(request):
    return HttpResponse('Каталог tops')
