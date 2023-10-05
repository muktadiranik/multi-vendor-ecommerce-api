from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import User
from . import choices




class User(AbstractUser):
    """
    Default custom user model for govelo.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, null=True, max_length=255)
    user_image = models.ImageField(
        upload_to='users/images', blank=True, null=True)
    street = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    area_code = models.CharField(max_length=20, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    user_cover = models.ImageField(
        upload_to='users/images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    role = models.CharField(max_length=20, choices=choices.ROLE_TYPE_CHOICES)

    def __str__(self):
        return self.user.username


class UserDocument(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    document = models.FileField(
        upload_to='users/documents', blank=True, null=True)

    def __str__(self):
        return self.user.username
