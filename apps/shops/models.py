import os
from slugify import slugify
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator
from apps.utilities.validators import *
from apps.setup.choices import *
from apps.setup.models import *
from django.contrib.auth import get_user_model
from django_quill.fields import QuillField

User = get_user_model()


def shop_directory_path(instance, filename):
    shop_name = slugify(instance.name)
    _, extension = os.path.splitext(filename)
    return f"shops/profile/{shop_name}{extension}"


def shop_cover_directory_path(instance, filename):
    shop_name = slugify(instance.name)
    _, extension = os.path.splitext(filename)
    return f"shops/cover/{shop_name}{extension}"


class Shop(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    legal_entity = models.CharField(max_length=50, blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.CharField(max_length=50, blank=True, null=True)
    area_code = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    website = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    shop_image = models.ImageField(upload_to=shop_directory_path, blank=True, null=True)
    shop_cover = models.ImageField(upload_to=shop_cover_directory_path, blank=True, null=True,)
    opening_time = models.TimeField(blank=True, null=True)
    closing_time = models.TimeField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True, default=0,
                               validators=[MaxValueValidator(5), MinValueValidator(0)])
    total_reviews = models.IntegerField(default=0, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    # terms_and_condition = QuillField(blank=True, null=True)
    terms_and_condition = models.TextField(blank=True, null=True)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.rating is None:
            self.rating = 0
        if self.total_reviews is None:
            self.total_reviews = 0
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['id']


class PickUpLocation(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.CharField(max_length=50, blank=True, null=True)
    area_code = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.shop.name

    class Meta:
        ordering = ['id']


class ShopVerification(models.Model):
    shop = models.OneToOneField(Shop, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=50, choices=SHOP_VERIFICATION_STATUS, default=SHOP_VERIFICATION_STATUS[0][0])
    owner_image = models.ImageField(upload_to="shops/verification/owner", null=True)
    id_front_image = models.ImageField(upload_to="shops/verification/id_front",
                                       validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])], null=True)
    id_back_image = models.ImageField(upload_to="shops/verification/id_back",
                                      validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])], null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.shop.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.status == SHOP_VERIFICATION_STATUS[0][0]:
            self.shop.is_verified = False
            self.shop.save()
        if self.status == SHOP_VERIFICATION_STATUS[1][0]:
            self.shop.is_verified = True
            self.shop.save()
        if self.status == SHOP_VERIFICATION_STATUS[2][0]:
            self.shop.is_verified = False
            self.shop.save()
