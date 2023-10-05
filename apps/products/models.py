import os
from slugify import slugify
from django.db import models
from apps.setup.models import *
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django_quill.fields import QuillField
from apps.utilities.validators import *
from apps.shops.models import Shop

User = get_user_model()


def product_directory_path(instance, filename):
    product_name = slugify(instance.model)
    _, extension = os.path.splitext(filename)
    return f"Products/{product_name}{extension}"


# def product_multi_directory_path(instance, filename):
#     product_name = slugify(instance.product.model)
#     _, extension = os.path.splitext(filename)
#     return f"Products/{product_name}{extension}"


class ProductSize(models.Model):
    product_size = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_size


class Product(models.Model):
    brand = models.CharField(max_length=50, blank=True, null=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, blank=True, null=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    # description = QuillField(blank=True, null=True)
    stock = models.BigIntegerField(blank=True, null=True)
    condition = models.CharField(max_length=100, blank=True, null=True)
    size = models.ForeignKey(ProductSize, on_delete=models.CASCADE, blank=True, null=True)
    is_available = models.BooleanField(default=True)
    # deposit = models.DecimalField(max_digits=10, decimal_places=2, blank=True,
    #                               null=True, verbose_name="Security Deposit",)
    rating = models.FloatField(blank=True, null=True, default=0,
                               validators=[MaxValueValidator(5), MinValueValidator(0)])
    total_reviews = models.BigIntegerField(blank=True, null=True, default=0)
    image = models.ImageField(upload_to=product_directory_path, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        if self.brand and self.model:
            return self.model + " " + self.brand
        return str(self.id)

    def save(self, *args, **kwargs):
        if self.stock == 0 or self.stock is None:
            self.is_available = False
        else:
            self.is_available = True

        if self.rating is None:
            self.rating = 0.0
        super().save(*args, **kwargs)


# class ProductImage(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
#     image = models.ImageField(upload_to=product_multi_directory_path, blank=True, null=True)
#     is_default = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         if self.product.brand and self.product.model:
#             return self.product.model + " " + self.product.brand
#         return str(self.id)


class ProductDeposit(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    deposit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.product.brand and self.product.model:
            return self.product.model + " " + self.product.brand
        return str(self.id)


class ProductRate(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    rate_type = models.ForeignKey(ProductRateType, on_delete=models.CASCADE, blank=True, null=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, blank=True, null=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.product.brand and self.product.model:
            return self.product.brand + " " + self.product.model
        return str(self.id)


class ProductOption(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    option = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.product.brand and self.product.model:
            return self.product.model + " " + self.product.brand
        return str(self.id)


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    review = models.TextField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True, default=0,
                               validators=[MaxValueValidator(5), MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.product.brand and self.product.model:
            return self.product.model + " " + self.product.brand
        return str(self.id)

    class Meta:
        ordering = ['-id']


class ProductDamage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='damage/products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.model + " " + self.product.brand
