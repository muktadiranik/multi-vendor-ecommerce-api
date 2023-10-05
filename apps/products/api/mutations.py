import pprint
import graphene
from django.db import transaction
from apps.products.models import *
from apps.products.api.schema import *
from apps.products.api.inputs import *
from apps.setup.models import ProductType
from apps.setup.models import *


class CreateProduct(graphene.Mutation):
    class Arguments:
        input = CreateProductInput()

    success = graphene.Boolean()
    product = graphene.Field(ProductObjectType)

    @staticmethod
    def mutate(root, info, input=None):
        success = True
        with transaction.atomic():
            if input.shop:
                shop = Shop.objects.get(pk=input.shop)
            else:
                shop = None
            if input.product_type:
                product_type = ProductType.objects.get(pk=input.product_type)
            else:
                product_type = None
            if input.size:
                size = ProductSize.objects.get(pk=input.size)
            else:
                size = None
            product_instance = Product(
                brand=input.brand,
                model=input.model,
                description=input.description,
                shop=shop,
                stock=input.stock,
                size=size,
                condition=input.condition,
                image=input.image,
                product_type=product_type,
            )
            product_instance.save()
            if input.prices:
                for rate in input.prices:
                    product_rate = ProductRate(
                        product=product_instance,
                        rate_type=ProductRateType.objects.get(pk=rate['rate_type']),
                        currency=Currency.objects.get(pk=rate['currency']),
                        rate=rate['rate']
                    )
                    product_rate.save()
            if input.deposit:
                for i in input.deposit:
                    product_deposit = ProductDeposit(
                        product=product_instance,
                        currency=Currency.objects.get(pk=i['currency']),
                        deposit=i['deposit']
                    )
                    product_deposit.save()
            return CreateProduct(success=success, product=product_instance)


class UpdateProduct(graphene.Mutation):
    class Arguments:
        id = graphene.String()
        input = UpdateProductInput()

    success = graphene.Boolean()
    product = graphene.Field(ProductObjectType)

    @staticmethod
    def mutate(root, info, id, input=None):
        success = False
        with transaction.atomic():
            product_instance = Product.objects.get(pk=id)
            if product_instance:
                success = True
                if input.brand:
                    product_instance.brand = input.brand
                if input.model:
                    product_instance.model = input.model
                if input.description:
                    product_instance.description = input.description
                if input.shop:
                    product_instance.shop = Shop.objects.get(pk=input.shop)
                if input.stock:
                    product_instance.stock = input.stock
                if input.product_type:
                    product_instance.product_type = ProductType.objects.get(pk=input.product_type)
                if input.size:
                    product_instance.size = ProductSize.objects.get(pk=input.size)
                if input.condition:
                    product_instance.condition = input.condition
                if input.image:
                    product_instance.image = input.image
                if input.deposit:
                    product_instance.deposit = input.deposit
                product_instance.save()
                if input.prices:
                    for rate in input.prices:
                        product_rate = ProductRate.objects.filter(
                            product=product_instance, rate_type=rate['rate_type'], currency=rate['currency'])
                        for i in product_rate:
                            i.rate = rate['rate']
                            i.currency = Currency.objects.get(pk=rate['currency'])
                            i.rate_type = ProductRateType.objects.get(pk=rate['rate_type'])
                            i.save()
                if input.deposit:
                    for i in input.deposit:
                        product_deposit = ProductDeposit.objects.filter(
                            product=product_instance, currency=i['currency'])
                        for j in product_deposit:
                            j.deposit = i['deposit']
                            j.currency = Currency.objects.get(pk=i['currency'])
                            j.save()
                return UpdateProduct(success=success, product=product_instance)
        return UpdateProduct(success=success, product=None)


class DeleteProduct(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id):
        success = False
        product_instance = Product.objects.get(pk=id)
        if product_instance:
            success = True
            product_instance.delete()
            return DeleteProduct(success=success)
        return DeleteProduct(success=success)


# class CreateProductImage(graphene.Mutation):
#     class Arguments:
#         input = CreateProductImageInput(required=True)

#     success = graphene.Boolean()
#     product_image = graphene.Field(ProductImageObjectType)

#     @staticmethod
#     def mutate(root, info, input=None):
#         success = True
#         product_image_instance = ProductImage(
#             product=Product.objects.get(pk=input.product),
#             image=input.image,
#             is_default=input.is_default,
#         )
#         product_image_instance.save()
#         return CreateProductImage(success=success, product_image=product_image_instance)


# class UpdateProductImage(graphene.Mutation):
#     class Arguments:
#         id = graphene.ID(required=True)
#         input = UpdateProductImageInput(required=True)

#     success = graphene.Boolean()
#     product_image = graphene.Field(ProductImageObjectType)

#     @staticmethod
#     def mutate(root, info, id, input=None):
#         success = False
#         product_image_instance = ProductImage.objects.get(pk=id)
#         if product_image_instance:
#             success = True
#             if input.product:
#                 product_image_instance.product = Product.objects.get(pk=input.product)
#             product_image_instance.image = input.image
#             product_image_instance.is_default = input.is_default
#             product_image_instance.save()
#             return UpdateProductImage(success=success, product_image=product_image_instance)
#         return UpdateProductImage(success=success, product_image=None)


# class DeleteProductImage(graphene.Mutation):
#     class Arguments:
#         id = graphene.ID(required=True)

#     success = graphene.Boolean()

#     @staticmethod
#     def mutate(root, info, id):
#         success = False
#         product_image_instance = ProductImage.objects.get(pk=id)
#         if product_image_instance:
#             success = True
#             product_image_instance.delete()
#             return DeleteProductImage(success=success)
#         return DeleteProductImage(success=success)


class CreateProductRate(graphene.Mutation):
    class Arguments:
        input = CreateProductRateInput(required=True)

    success = graphene.Boolean()
    product_rate = graphene.Field(ProductRateObjectType)

    @staticmethod
    def mutate(root, info, input=None):
        success = True
        product_rate_instance = ProductRate(
            product=Product.objects.get(pk=input.product),
            rate_type=ProductRateType.objects.get(pk=input.rate_type),
            rate=input.rate,
        )
        product_rate_instance.save()
        return CreateProductRate(success=success, product_rate=product_rate_instance)


class UpdateProductRate(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = UpdateProductRateInput(required=True)

    success = graphene.Boolean()
    product_rate = graphene.Field(ProductRateObjectType)

    @staticmethod
    def mutate(root, info, id, input=None):
        success = False
        product_rate_instance = ProductRate.objects.get(pk=id)
        if product_rate_instance:
            success = True
            if input.product:
                product_rate_instance.product = Product.objects.get(pk=input.product)
            if input.rate_type:
                product_rate_instance.rate_type = ProductRateType.objects.get(pk=input.rate_type)
            product_rate_instance.rate = input.rate
            product_rate_instance.save()
            return UpdateProductRate(success=success, product_rate=product_rate_instance)
        return UpdateProductRate(success=success, product_rate=None)


class DeleteProductRate(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id):
        success = False
        product_rate_instance = ProductRate.objects.get(pk=id)
        if product_rate_instance:
            success = True
            product_rate_instance.delete()
            return DeleteProductRate(success=success)
        return DeleteProductRate(success=success)


class CreateProductOption(graphene.Mutation):
    class Arguments:
        input = CreateProductOptionInput(required=True)

    success = graphene.Boolean()
    product_option = graphene.Field(ProductOptionObjectType)

    @staticmethod
    def mutate(root, info, input=None):
        success = True
        product_option_instance = ProductOption(
            product=Product.objects.get(pk=input.product),
            option=input.option,
        )
        product_option_instance.save()
        return CreateProductOption(success=success, product_option=product_option_instance)


class UpdateProductOption(graphene.Mutation):
    class Arguments:
        input = CreateProductOptionInput(required=True)
        id = graphene.ID(required=True)

    success = graphene.Boolean()
    product_option = graphene.Field(ProductOptionObjectType)

    @staticmethod
    def mutate(root, info, id, input=None):
        success = False
        product_option_instance = ProductOption.objects.get(pk=id)
        if product_option_instance:
            success = True
            if input.product:
                product_option_instance.product = Product.objects.get(pk=input.product)
            product_option_instance.option = input.option
            product_option_instance.save()
            return UpdateProductOption(success=success, product_option=product_option_instance)
        return UpdateProductOption(success=success, product_option=None)


class DeleteProductOption(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id):
        success = False
        product_option_instance = ProductOption.objects.get(pk=id)
        if product_option_instance:
            success = True
            product_option_instance.delete()
            return DeleteProductOption(success=success)
        return DeleteProductOption(success=success)


class CreateProductReview(graphene.Mutation):
    class Arguments:
        input = CreateProductReviewInput(required=True)

    success = graphene.Boolean()
    product_review = graphene.Field(ProductReviewObjectType)

    @staticmethod
    def mutate(root, info, input=None):

        success = True
        product_review_instance = ProductReview(
            product=Product.objects.get(pk=input.product),
            user=User.objects.get(pk=input.user),
            review=input.review,
            rating=input.rating,
        )
        product_review_instance.save()
        return CreateProductReview(success=success, product_review=product_review_instance)


class UpdateProductReview(graphene.Mutation):
    class Arguments:
        input = CreateProductReviewInput(required=True)
        id = graphene.ID(required=True)

    success = graphene.Boolean()
    product_review = graphene.Field(ProductReviewObjectType)

    @staticmethod
    def mutate(root, info, id, input=None):
        success = False
        product_review_instance = ProductReview.objects.get(pk=id)
        if product_review_instance:
            success = True
            if input.product:
                product_review_instance.product = Product.objects.get(pk=input.product)
            if input.user:
                product_review_instance.user = User.objects.get(pk=input.user)
            product_review_instance.review = input.review
            product_review_instance.rating = input.rating
            product_review_instance.save()
            return UpdateProductReview(success=success, product_review=product_review_instance)
        return UpdateProductReview(success=success, product_review=None)


class DeleteProductReview(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id):
        success = False
        product_review_instance = ProductReview.objects.get(pk=id)
        if product_review_instance:
            success = True
            product_review_instance.delete()
            return DeleteProductReview(success=success)
        return DeleteProductReview(success=success)


class CreateProductDamage(graphene.Mutation):
    class Arguments:
        input = CreateProductDamageInput(required=True)

    success = graphene.Boolean()
    product_damage = graphene.Field(ProductDamageObjectType)

    @staticmethod
    def mutate(root, info, input=None):

        success = True
        product_damage_instance = ProductDamage.objects.create()
        product_damage_instance.product = Product.objects.get(pk=input.product)
        product_damage_instance.user = User.objects.get(pk=input.user)
        product_damage_instance.description = input.description
        product_damage_instance.save()
        return CreateProductDamage(success=success, product_damage=product_damage_instance)


class UpdateProductDamage(graphene.Mutation):
    class Arguments:
        input = CreateProductDamageInput(required=True)
        id = graphene.ID(required=True)

    success = graphene.Boolean()
    product_damage = graphene.Field(ProductDamageObjectType)

    @staticmethod
    def mutate(root, info, id, input=None):
        success = False
        product_damage_instance = ProductDamage.objects.get(pk=id)
        if product_damage_instance:
            success = True
            if input.product:
                product_damage_instance.product = Product.objects.get(pk=input.product)
            if input.user:
                product_damage_instance.user = User.objects.get(pk=input.user)
            product_damage_instance.description = input.description
            product_damage_instance.save()
            return UpdateProductDamage(success=success, product_damage=product_damage_instance)
        return UpdateProductDamage(success=success, product_damage=None)


class DeleteProductDamage(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id):
        success = False
        product_damage_instance = ProductDamage.objects.get(pk=id)
        if product_damage_instance:
            success = True
            product_damage_instance.delete()
            return DeleteProductDamage(success=success)
        return DeleteProductDamage(success=success)


class ProductMutation(graphene.ObjectType):
    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
    delete_product = DeleteProduct.Field()
    # create_product_image = CreateProductImage.Field()
    # update_product_image = UpdateProductImage.Field()
    # delete_product_image = DeleteProductImage.Field()
    create_product_rate = CreateProductRate.Field()
    update_product_rate = UpdateProductRate.Field()
    delete_product_rate = DeleteProductRate.Field()
    create_product_option = CreateProductOption.Field()
    update_product_option = UpdateProductOption.Field()
    delete_product_option = DeleteProductOption.Field()
    create_product_review = CreateProductReview.Field()
    update_product_review = UpdateProductReview.Field()
    delete_product_review = DeleteProductReview.Field()
    create_product_damage = CreateProductDamage.Field()
    update_product_damage = UpdateProductDamage.Field()
    delete_product_damage = DeleteProductDamage.Field()
