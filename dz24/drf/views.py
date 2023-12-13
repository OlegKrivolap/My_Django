from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.response import Response

# Create your views ere.


class CarAPIView(APIView):
    def get(self,request,*args,**kwargs):
        queryset = Car.objects.all()
        serializer = CarSerializer(queryset, many=True)
        return Response(serializer.data)

class SearchView(APIView):
    def get(self, request):
        query = request.query_params.get('q')
        articles = Car.objects.filter(name__icontains=query)
        serializer = CarSerializer(articles, many=True)
        return Response(serializer.data)