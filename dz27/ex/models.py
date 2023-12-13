from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/', null=True)
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.name
