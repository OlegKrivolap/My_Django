from django.shortcuts import render
from rest_framework.views import *
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import generics
from .export import *
from django.http import HttpResponse
from django.views.generic import *
from .models import *
from .forms import *
from .admin import *
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




