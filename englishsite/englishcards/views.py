from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def get_home(request):
    return HttpResponse('Head page')


def get_cards(request):
    return HttpResponse('Cards page')


def get_words(request):
    return HttpResponse('Words')
