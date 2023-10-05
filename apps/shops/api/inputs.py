import graphene
from apps.shops.models import *
from apps.shops.api.schema import *
from graphene_file_upload.scalars import Upload
from django_quill.fields import QuillField


class CreatePickupLocationInput(graphene.InputObjectType):
    country = graphene.String()
    street = graphene.String()
    city = graphene.String()
    state = graphene.String()
    zip_code = graphene.String()
    area_code = graphene.String()
    latitude = graphene.Decimal()
    longitude = graphene.Decimal()


class UpdatePickupLocationInput(graphene.InputObjectType):
    id = graphene.ID(required=True)
    country = graphene.String()
    street = graphene.String()
    city = graphene.String()
    state = graphene.String()
    zip_code = graphene.String()
    area_code = graphene.String()
    latitude = graphene.Decimal()
    longitude = graphene.Decimal()


class CreateShopInput(graphene.InputObjectType):
    user_id = graphene.ID()
    name = graphene.String()
    legal_entity = graphene.String()
    street = graphene.String()
    city = graphene.String()
    state = graphene.String()
    zip_code = graphene.String()
    area_code = graphene.String()
    country = graphene.String()
    latitude = graphene.Decimal()
    longitude = graphene.Decimal()
    phone = graphene.String()
    website = graphene.String()
    email = graphene.String()
    description = graphene.String()
    shop_image = Upload()
    shop_cover = Upload()
    opening_time = graphene.Time()
    closing_time = graphene.Time()
    terms_and_condition = QuillField()
    pickup_locations = graphene.List(CreatePickupLocationInput)


class UpdateShopInput(graphene.InputObjectType):
    id = graphene.ID(required=True)
    name = graphene.String()
    legal_entity = graphene.String()
    street = graphene.String()
    city = graphene.String()
    state = graphene.String()
    zip_code = graphene.String()
    area_code = graphene.String()
    country = graphene.String()
    latitude = graphene.Decimal()
    longitude = graphene.Decimal()
    phone = graphene.String()
    website = graphene.String()
    email = graphene.String()
    description = graphene.String()
    shop_image = Upload()
    shop_cover = Upload()
    opening_time = graphene.Time()
    closing_time = graphene.Time()
    terms_and_condition = QuillField()
    pickup_locations = graphene.List(UpdatePickupLocationInput)


class CreateShopVerificationInput(graphene.InputObjectType):
    shop_id = graphene.ID()
    owner_image = Upload()
    id_front_image = Upload()
    id_back_image = Upload()


class UpdateShopVerificationInput(graphene.InputObjectType):
    id = graphene.ID(required=True)
    owner_image = Upload()
    id_front_image = Upload()
    id_back_image = Upload()
