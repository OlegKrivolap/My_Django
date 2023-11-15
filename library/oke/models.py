from django.db import models


# Create your models here.

class Libraries(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    author = models.ManyToManyField('Authors', name='author')

    def __str__(self):
        return self.name


class Authors(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Books(models.Model):
    author_1 = models.ForeignKey('Authors', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
