from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from apps.products.models import *
from apps.shops.models import *

User = get_user_model()


@receiver(post_save, sender=Product)
def create_or_update_shop_rating(sender, instance, **kwargs):
    shop = get_object_or_404(Shop, id=instance.shop.id)
    shop.rating = shop.product_set.prefetch_related('productreview_set').aggregate(
        models.Avg('productreview__rating'))['productreview__rating__avg']
    shop_total_reviews = 0
    for i in shop.product_set.all():
        shop_total_reviews = shop_total_reviews + i.total_reviews
    shop.total_reviews = shop_total_reviews
    shop.save()
