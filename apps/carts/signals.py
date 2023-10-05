from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from apps.carts.models import *

User = get_user_model()


@receiver(post_save, sender=User)
def create_cart_on_user_create(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)
