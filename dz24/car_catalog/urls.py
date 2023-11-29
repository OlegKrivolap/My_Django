from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('forms/<int:forms_id>/', get_forms, name='forms'),
    path('car/<int:car_id>/', get_one_car, name = 'get_car'),
]
