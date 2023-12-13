from django.db.models.signals import post_save, post_delete
from .models import *
from django.dispatch import receiver
from .bot import *




@receiver(post_save, sender=Car)
def post_save_data(sender, **kwargs):
    bot_save()

