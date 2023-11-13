from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', home, name = 'home'),
                  path('rose/', get_bouquets, name='get-bouquets'),
                  path('rose/card/<int:name_id>', get_card, name='get-card')

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
