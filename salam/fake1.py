import django
django.setup()
from test1.models import *
from faker import Faker





fake = Faker()

def get_data(value):
    for i in range(value):
        name = fake.name()
        adres = fake.address()
        obj = Person.objects.get_or_create(name=name, adres=adres)


def main():
    no = int(input('number'))
    get_data(no)


if __name__ == '__main__':
    main()