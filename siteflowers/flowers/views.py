from django.shortcuts import render
from django.http import HttpResponse
from flowers.models import Flowers


# Create your views here.
def home(request):
    flow = Flowers.objects.all()
    context = {'title':'Главная страница', 'flow': flow}
    return render(request, 'base1.html', context=context)

def get_bouquets(request):
    flow = Flowers.objects.filter(title__contains = 'укет')
    context = {'flow' : flow}
    return render(request, 'bouquets.html', context=context)

def get_card(request, name_id):
    flow = Flowers.objects.filter(id = name_id)
    context ={'flow': flow}
    return render(request, 'content.html', context=context)

