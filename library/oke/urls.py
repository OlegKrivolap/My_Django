from django.urls import path
from .views import *

urlpatterns = [
    path('', get_libraries, name = 'lib'),
    path('authors/', get_authors),
    path('book/', BookForm.as_view(), name = 'book')
]