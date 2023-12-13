from django.shortcuts import render
from .serializers import *
from rest_framework import generics
from django.http import HttpResponse
from django.views.generic import *
from .admin import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# Create your views here.

def home(request):
    cars = Car.objects.all()
    context = {'cars':cars}
    return render(request, 'home.html', context=context)
class CarAPIView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class GetListView(ListView, FormView):
    model = Car
    template_name = 'home.html'

    def post(self, request, *args, **kwargs):
        qs = self.get_queryset()
        dataset = CarResources().export()
        format = dataset.xls
        # format = request.POST.get('format')

        # if format == 'xls':
        #     ds = dataset.xls
        # elif format == 'csv':
        #     ds = dataset.csv
        # else:
        #     ds = dataset.json

        response = HttpResponse(format, content_type=f'xls')
        response['Content-Disposition'] = f"attachment; filename=Cars.xls"
        return response


class SignUpView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class CustomLogoutView(LogoutView):
    pass