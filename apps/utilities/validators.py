from django.core.exceptions import ValidationError
from PIL import Image
from django.utils.translation import gettext_lazy as _
from apps.shops.models import *
from apps.products.models import *


def validate_shop_image_size(image):
    with Image.open(image) as img:
        width, height = img.size
        if width != 100 or height != 100:
            raise ValidationError("The image size must be 100x100 px.")


def validate_shop_cover_size(image):
    with Image.open(image) as img:
        width, height = img.size
        if width != 1300 or height != 145:
            raise ValidationError("The image size must be 1300x145 px.")


def validate_product_image_size(image):
    with Image.open(image) as img:
        width, height = img.size
        if width != 745 or height != 500:
            raise ValidationError("The image size must be 745x500 px.")


def validate_site_icon_size(image):
    with Image.open(image) as img:
        width, height = img.size
        if width != 100 or height != 100:
            raise ValidationError("The image size must be 100x100 px.")


def validate_site_video_size(video):
    if video.size > 10000000:
        raise ValidationError("The video size must be less than 10MB.")

    if video.width != 1280 or video.height != 720:
        raise ValidationError("The video size must be 1280x720 px.")


# def CaseInsensitiveUsernameValidator(value):
#     if User.objects.filter(username__iexact=value).exists():
#         raise ValidationError(
#             _('%(value)s is already in use.'),
#             params={'value': value},
#         )
