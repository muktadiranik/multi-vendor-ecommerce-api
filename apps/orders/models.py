from django.db import models
from apps.products.models import *
from apps.setup.choices import *
import uuid as uuid_lib
from django.contrib.auth import get_user_model

User = get_user_model()


def rental_numbers():
    return uuid_lib.uuid4().hex[:8].upper()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    rental_number = models.CharField(max_length=50, default=rental_numbers, unique=True, null=True, blank=True)
    payment_method = models.CharField(max_length=50, null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    paid_at = models.DateTimeField(null=True, blank=True)
    delivered_at = models.DateTimeField(null=True, blank=True)
    returned_at = models.DateTimeField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True, default=0)
    status = models.CharField(choices=ORDER_STATUS, max_length=50, null=True, blank=True, default=ORDER_STATUS[0][0])
    is_cancelled = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['-id']

    def save(self, *args, **kwargs):
        if self.is_paid:
            self.status = ORDER_STATUS[1][0]
        if self.is_delivered:
            self.status = ORDER_STATUS[2][0]
        if self.is_cancelled == True:
            self.status = ORDER_STATUS[3][0]
        if self.refund_requested == True:
            self.status = ORDER_STATUS[4][0]
        super().save(*args, **kwargs)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product.brand + " " + self.product.model)

    class Meta:
        ordering = ['-id']


class ShippingAddress(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=100, null=True, blank=True)
    area_code = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return (str(self.order.id) + " " + str(self.order.user.username))


class PaymentInformation(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    create_time = models.DateTimeField(null=True, blank=True)
    update_time = models.DateTimeField(null=True, blank=True)
    payment_id = models.CharField(max_length=100, null=True, blank=True)
    payment_order_id = models.CharField(max_length=100, null=True, blank=True)
    intent = models.CharField(max_length=100, null=True, blank=True)
    payer_country_code = models.CharField(max_length=100, null=True, blank=True)
    payer_email = models.CharField(max_length=100, null=True, blank=True)
    payer_id = models.CharField(max_length=100, null=True, blank=True)
    payer_name = models.CharField(max_length=100, null=True, blank=True)
    purchase_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    purchase_currency_code = models.CharField(max_length=100, null=True, blank=True)
    purchase_units_reference_id = models.CharField(max_length=100, null=True, blank=True)
    purchase_shipping_address = models.JSONField(null=True, blank=True)
    purchase_shipping_name = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return (str(self.order.id) + " " + str(self.order.user.username))


class Refund(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=True)
    reason = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True, choices=REFUND_STATUS, default=REFUND_STATUS[0][0])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (str(self.order.id) + " " + str(self.order.user.username))

    class Meta:
        ordering = ['-id']

    def save(self, *args, **kwargs):
        if self.status == REFUND_STATUS[1][0]:
            self.order.refund_requested = True
            self.order.save()
        super().save(*args, **kwargs)
