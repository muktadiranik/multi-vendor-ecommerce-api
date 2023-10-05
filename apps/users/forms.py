from allauth.account.utils import (filter_users_by_email,
                                   user_pk_to_url_str, user_username)
from allauth.account.forms import default_token_generator
from allauth.account.adapter import get_adapter
from rest_framework.exceptions import ValidationError
from django.template.loader import render_to_string
import environ
from django.core.mail import send_mail
from dj_rest_auth.forms import AllAuthPasswordResetForm
from allauth.utils import build_absolute_uri
from allauth.account.utils import user_pk_to_url_str, user_username
from allauth.account import app_settings
from django.urls.base import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

User = get_user_model()
env = environ.Env()


class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }


class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """


class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """


class CustomAllAuthPasswordResetForm(AllAuthPasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data["email"]
        email = get_adapter().clean_email(email)
        self.users = filter_users_by_email(email, is_active=True)
        try:
            user = User.objects.get(email=email)
            if user:
                return self.cleaned_data["email"]
        except:
            raise ValidationError([{'email': "e-mail has not been registered"}])

    def save(self, request, **kwargs):
        current_site = get_current_site(request)
        email = self.cleaned_data['email']
        token_generator = kwargs.get('token_generator', default_token_generator)

        for user in self.users:
            temp_key = token_generator.make_token(user)
            path = reverse(
                'password_reset_confirm',
                args=[user_pk_to_url_str(user), temp_key],
            )
            url = build_absolute_uri(None, path)
            context = {
                'current_site': current_site,
                'user': user,
                'password_reset_url': url,
                'request': request,
            }
            if app_settings.AUTHENTICATION_METHOD != app_settings.AuthenticationMethod.EMAIL:
                context['username'] = user_username(user)
            send_mail(
                subject='Go-Velo Password Reset',
                message='password reset email',
                from_email=env("DEFAULT_FROM_EMAIL"),
                recipient_list=[email],
                html_message=render_to_string('email/password_reset_email.html', context),
            )
        return self.cleaned_data['email']
