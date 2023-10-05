from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from apps.products.models import *
from apps.orders.models import *

User = get_user_model()


@receiver(post_save, sender=ProductReview)
def create_or_update_product_rating(sender, instance, **kwargs):
    product = get_object_or_404(Product, id=instance.product.id)
    product.rating = product.productreview_set.aggregate(models.Avg('rating'))['rating__avg']
    product.total_reviews = product.productreview_set.count()
    product.save()
    


# @receiver(post_save, sender=ProductStock)
# def create_or_update_product_stock(sender, instance, **kwargs):
#     product = get_object_or_404(Product, id=instance.product.id)
#     product.stock = product.productstock.stock
#     product.save()
#     print("Product stock updated")


@receiver(post_save, sender=OrderItem)
def create_or_update_product_stock_by_order_item(sender, instance, **kwargs):
    product = get_object_or_404(Product, id=instance.product.id)
    if instance.order.is_paid is True or instance.order.is_delivered is True:
        product.stock = product.stock - instance.quantity
        product.save()
      
