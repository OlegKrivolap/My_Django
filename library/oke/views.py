from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def get_libraries(request):
    w1 = Libraries.objects.get(name = 'Библиотека № 17')
    authors = w1.author.all()
    context = {'w1': w1, 'authors': authors}
    return render(request, template_name='new.html', context=context)

def get_authors(request):
    w1 = Authors.objects.all()
    context = {'w1': w1}
    return render(request, template_name='authors.html', context=context)