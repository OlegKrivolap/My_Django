from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.db.models import Avg, Min, Max, Count
from .forms import *

# Create your views here.
def get_libraries(request):
    w1 = Libraries.objects.get(name = 'Библиотека № 17')
    authors = w1.author.all()
    context = {'w1': w1, 'authors': authors}
    return render(request, template_name='new.html', context=context)

def get_authors(request):
    avg = Books.objects.aggregate(Avg('price'))['price__avg']
    min_1 = Books.objects.aggregate(Min('price'))['price__min']
    max_1 = Books.objects.aggregate(Max('price'))['price__max']
    all = Books.objects.aggregate(Count('name'))['name__count']
    context = {'avg': avg, 'min': min_1, 'max': max_1, 'all': all}
    return render(request, template_name='authors.html', context=context)




class BookForm(CreateView):
    template_name = 'forms.html'
    form_class = BookForm
    success_url = ('/')