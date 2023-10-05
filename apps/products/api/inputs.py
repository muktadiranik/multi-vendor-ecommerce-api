import graphene
from apps.products.models import *
from apps.products.api.schema import *
from graphene_file_upload.scalars import Upload
from django_quill.fields import QuillField


class CreateProductRateInput(graphene.InputObjectType):
    rate_type = graphene.ID()
    rate = graphene.Decimal()
    currency = graphene.ID()


class UpdateProductRateInput(graphene.InputObjectType):
    rate_type = graphene.ID()
    rate = graphene.Decimal()
    currency = graphene.ID()


class CreateProductDepositInput(graphene.InputObjectType):
    currency = graphene.ID()
    deposit = graphene.Decimal()


class UpdateProductDepositInput(graphene.InputObjectType):
    currency = graphene.ID()
    deposit = graphene.Decimal()


# class CreateProductImageInput(graphene.InputObjectType):
#     product = graphene.ID()
#     image = Upload()
#     is_default = graphene.Boolean()


# class UpdateProductImageInput(graphene.InputObjectType):
#     product = graphene.ID()
#     is_default = graphene.Boolean()
#     image = Upload()


class CreateProductInput(graphene.InputObjectType):
    brand = graphene.String()
    model = graphene.String()
    product_type = graphene.ID()
    shop = graphene.ID()
    description = graphene.String()
    # description = QuillField()
    stock = graphene.Int()
    size = graphene.ID()
    condition = graphene.String()
    prices = graphene.List(CreateProductRateInput)
    # deposit = graphene.Decimal()
    deposit = graphene.List(CreateProductDepositInput)
    image = Upload()


class UpdateProductInput(graphene.InputObjectType):
    brand = graphene.String()
    model = graphene.String()
    product_type = graphene.ID()
    shop = graphene.ID()
    description = graphene.String()
    # description = QuillField()
    stock = graphene.Int()
    size = graphene.ID()
    condition = graphene.String()
    prices = graphene.List(UpdateProductRateInput)
    # deposit = graphene.Decimal()
    deposit = graphene.List(UpdateProductDepositInput)
    image = Upload()


class CreateProductOptionInput(graphene.InputObjectType):
    product = graphene.ID()
    option = graphene.String()


class CreateProductConditionInput(graphene.InputObjectType):
    product = graphene.ID()
    condition = graphene.String()


class UpdateProductConditionInput(graphene.InputObjectType):
    product = graphene.ID()
    condition = graphene.String()


class CreateProductReviewInput(graphene.InputObjectType):
    user = graphene.ID()
    product = graphene.ID()
    review = graphene.String()
    rating = graphene.Int()


class UpdateProductReviewInput(graphene.InputObjectType):
    User = graphene.ID()
    product = graphene.ID()
    review = graphene.String()
    rating = graphene.Int()


class CreateProductDamageInput(graphene.InputObjectType):
    user = graphene.ID()
    product = graphene.ID()
    description = graphene.String()
    image = Upload()


class UpdateProductDamageInput(graphene.InputObjectType):
    user = graphene.ID()
    product = graphene.ID()
    description = graphene.String()
    image = Upload()
