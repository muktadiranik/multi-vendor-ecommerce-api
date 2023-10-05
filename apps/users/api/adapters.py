from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from typing import Any
from django.conf import settings
from django.http import HttpRequest
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
import environ

env = environ.Env()
User = get_user_model()


class CustomDefaultAccountAdapter(DefaultAccountAdapter):
    def send_mail(self, template_prefix, email, context):
        context['activate_url'] = env("FRONTEND_URL") + "/account-confirm-email/" + str(context["key"])
        context["username"] = User.objects.get(email=email).username
        send_mail(
            subject='Go-Velo Confirmation Email',
            message='confirmation email',
            from_email=env("DEFAULT_FROM_EMAIL"),
            recipient_list=[email],
            html_message=render_to_string('email/confirmation_email.html', context),
        )


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def is_open_for_signup(self, request: HttpRequest, sociallogin: Any):
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)
    
    def pre_social_login(self, request, sociallogin):
        user = sociallogin.user
        user.username = user.email.split('@')[0]
        user.save()
        return super().pre_social_login(request, sociallogin)
    
    def save_user(self, request, sociallogin, form=None):
        user = sociallogin.user
        user.username = user.email.split('@')[0]
        user.save()
        return super().save_user(request, sociallogin, form)
    
    def social_auth_token(self, sociallogin):
        return sociallogin.token
    
    def populate_user(self, request, sociallogin, data):
        user = sociallogin.user
        user.username = user.email.split('@')[0]
        user.save()
        return super().populate_user(request, sociallogin, data)


