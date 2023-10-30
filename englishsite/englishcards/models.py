from django.db import models

# Create your models here.
class Cards(models.Model):
    words_en = models.CharField(max_length=255)
    words_ru = models.CharField(max_length=255)
    picture = models.ImageField
