from django.urls import path
from .views import *

urlpatterns = [
    path('', get_libraries),
    path('authors/', get_authors)
]