from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    w1 = Car.objects.all()
    context = {'w1':w1}
    return render(request, 'home.html', context=context)