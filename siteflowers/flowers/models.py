from django.db import models


# Create your models here.
class Flowers(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField(blank=True, upload_to='images')

    def __str__(self):
        return self.title
