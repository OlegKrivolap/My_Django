from django.urls import path
from .views import *

urlpatterns = [
    path('', CarAPIView.as_view(), name='home'),
    path('search/', SearchView.as_view(), name='home'),
]
