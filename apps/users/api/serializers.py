from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import PasswordResetSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from apps.users.models import *
from apps.users.forms import *

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("name", 'user_image', 'user_cover', 'street', 'city',
                  'state', 'zip_code', 'area_code', 'phone_number', 'country', 'created_at',)
        read_only_fields = ('created_at',)

    def validate_email(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value

    def validate_username(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError({"username": "This username is already in use."})
        return value

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.user_image = validated_data["user_image"]
        instance.street = validated_data["street"]
        instance.city = validated_data["city"]
        instance.state = validated_data["state"]
        instance.zip_code = validated_data["zip_code"]
        instance.area_code = validated_data["area_code"]
        instance.phone_number = validated_data["phone_number"]
        instance.country = validated_data["country"]
        instance.user_cover = validated_data["user_cover"]

        instance.save()

        return instance


class CustomPasswordResetSerializer(PasswordResetSerializer):
    @property
    def password_reset_form_class(self):
        return CustomAllAuthPasswordResetForm

  


class CustomRegisterSerializer(RegisterSerializer):
    pass
