from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home),
    path('cards/', views.get_cards),
    path('words/', views.get_words)
]
