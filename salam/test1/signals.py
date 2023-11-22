from django.db.models.signals import post_save, post_delete
from .models import Person
from django.dispatch import receiver
from .bot import *




@receiver(post_save, sender=Person)
def post_save_data(sender, **kwargs):
    bot_save()


@receiver(post_delete, sender=Person)
def post_save_data(sender, **kwargs):
    bot_delete()
