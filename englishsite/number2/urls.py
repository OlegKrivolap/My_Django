from django.urls import path
from .views import get_all_users, get_user, add_registration
urlpatterns = [
    path('all/',get_all_users, name='list-users'),
    path('one/', get_user, name='user-regist'),
    path('registration/', add_registration, name='registration')
]