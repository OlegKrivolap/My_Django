from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import *

# Create your views here.

def home(request):
    w1 = Car.objects.all()
    form = CarForm()
    context = {'w1':w1, 'form':form}
    return render(request, 'home.html', context=context)


def get_one_car(request,car_id):
    car = Car.objects.filter(pk = car_id)
    context = {'car':car}
    return render(request, 'solo.html',context=context )
def get_forms(request, forms_id):
    if request.method =='POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form=CarForm()
        car1 = Car.objects.filter(pk=forms_id)
    return render(request,'forms.html', {'form':form, 'car':car1})