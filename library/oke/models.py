from django.db import models


# Create your models here.


class Abstract(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True


class Libraries(Abstract):
    address = models.CharField(max_length=255)
    author = models.ManyToManyField('Authors', name='author')

    def __str__(self):
        return self.name


class Authors(Abstract):
    pass

    def __str__(self):
        return self.name


class Books(Abstract):
    author_1 = models.ForeignKey('Authors', on_delete=models.CASCADE, null=True)
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.name
