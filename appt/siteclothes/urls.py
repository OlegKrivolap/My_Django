from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('jeans/', views.jeans),
    path('tops/', views.tops)

]