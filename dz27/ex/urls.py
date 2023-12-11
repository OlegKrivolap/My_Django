from django.urls import path
from .views import *

# app_name = 'ex'
urlpatterns = [
    path('', home, name = 'home'),
    path('api', CarAPIView.as_view()),
    path('<int:pk>', CarAPIView.as_view()),
    path('download/', GetListView.as_view(), name = 'GetListView')
]