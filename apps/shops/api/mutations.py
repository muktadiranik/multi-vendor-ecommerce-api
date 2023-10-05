import graphene
import graphene_file_upload
from apps.shops.models import *
from apps.shops.api.schema import *
from apps.shops.api.inputs import *
from apps.users.models import *
from apps.setup.models import *


class CreateShop(graphene.Mutation):
    class Arguments:
        input = CreateShopInput(required=True)

    success = graphene.Boolean()
    shop = graphene.Field(ShopObjectType)

    @staticmethod
    def mutate(root, info, input=None):
        user = User.objects.get(id=input.user_id)
        success = True

        try:
            shop = Shop.objects.get(owner=user)
        except Shop.DoesNotExist:
            shop = Shop.objects.create(owner=user)
        try:
            if input.name:
                shop.name = input.name
            if input.legal_entity:
                shop.legal_entity = input.legal_entity
            if input.street:
                shop.street = input.street
            if input.city:
                shop.city = input.city
            if input.state:
                shop.state = input.state
            if input.zip_code:
                shop.zip_code = input.zip_code
            if input.area_code:
                shop.area_code = input.area_code
            if input.country:
                shop.country = input.country
            if input.latitude:
                shop.latitude = input.latitude
            if input.longitude:
                shop.longitude = input.longitude
            if input.phone:
                shop.phone = input.phone
            if input.website:
                shop.website = input.website
            if input.email:
                shop.email = input.email
            if input.description:
                shop.description = input.description
            if input.shop_image:
                shop.shop_image = input.shop_image
            if input.shop_cover:
                shop.shop_cover = input.shop_cover
            if input.opening_time:
                shop.opening_time = input.opening_time
            if input.closing_time:
                shop.closing_time = input.closing_time
            if input.terms_and_condition:
                shop.terms_and_condition = input.terms_and_condition
            if input.pickup_locations:
                for pickup_location in input.pickup_locations:
                    pickup_location_instance = PickUpLocation.objects.create(
                        shop=shop,
                        country=pickup_location.country,
                        street=pickup_location.street,
                        city=pickup_location.city,
                        state=pickup_location.state,
                        zip_code=pickup_location.zip_code,
                        area_code=pickup_location.area_code,
                        latitude=pickup_location.latitude,
                        longitude=pickup_location.longitude,
                    )
                pickup_location_instance.save()

            shop.save()
        except shop.DoesNotExist:
            success = False
            shop = None
        return CreateShop(success=success, shop=shop)


class UpdateShop(graphene.Mutation):
    class Arguments:
        input = UpdateShopInput(required=True)

    success = graphene.Boolean()
    shop = graphene.Field(ShopObjectType)

    @staticmethod
    def mutate(root, info, input=None):
        success = False
        shop_instance = Shop.objects.get(pk=input.id)
        if shop_instance:
            success = True

            if input.name:
                shop_instance.name = input.name
            if input.legal_entity:
                shop_instance.legal_entity = input.legal_entity
            if input.street:
                shop_instance.street = input.street
            if input.city:
                shop_instance.city = input.city
            if input.state:
                shop_instance.state = input.state
            if input.zip_code:
                shop_instance.zip_code = input.zip_code
            if input.area_code:
                shop_instance.area_code = input.area_code
            if input.country:
                shop_instance.country = input.country
            if input.latitude:
                shop_instance.latitude = input.latitude
            if input.longitude:
                shop_instance.longitude = input.longitude
            if input.phone:
                shop_instance.phone = input.phone
            if input.website:
                shop_instance.website = input.website
            if input.email:
                shop_instance.email = input.email
            if input.description:
                shop_instance.description = input.description
            if input.shop_image:
                shop_instance.shop_image = input.shop_image
            if input.shop_cover:
                shop_instance.shop_cover = input.shop_cover
            if input.opening_time:
                shop_instance.opening_time = input.opening_time
            if input.closing_time:
                shop_instance.closing_time = input.closing_time
            if input.terms_and_condition:
                shop_instance.terms_and_condition = input.terms_and_condition
            if input.pickup_locations:
                for pickup_location in input.pickup_locations:
                    pickup_location_instance = PickUpLocation.objects.get(
                        pk=pickup_location.id
                    )
                    if pickup_location.country:
                        pickup_location_instance.country = pickup_location.country
                    if pickup_location.street:
                        pickup_location_instance.street = pickup_location.street
                    if pickup_location.city:
                        pickup_location_instance.city = pickup_location.city
                    if pickup_location.state:
                        pickup_location_instance.state = pickup_location.state
                    if pickup_location.zip_code:
                        pickup_location_instance.zip_code = pickup_location.zip_code
                    if pickup_location.area_code:
                        pickup_location_instance.area_code = pickup_location.area_code
                    if pickup_location.latitude:
                        pickup_location_instance.latitude = pickup_location.latitude
                    if pickup_location.longitude:
                        pickup_location_instance.longitude = pickup_location.longitude
                    pickup_location_instance.save()

            shop_instance.save()
            return UpdateShop(success=success, shop=shop_instance)
        return UpdateShop(success=success, shop=None)


class DeleteShop(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id):
        success = False
        shop_instance = Shop.objects.get(pk=id)
        if shop_instance:
            success = True
            shop_instance.delete()
        return DeleteShop(success=success)


class CreateShopVerification(graphene.Mutation):
    class Arguments:
        input = CreateShopVerificationInput()

    success = graphene.Boolean()
    shop_verification = graphene.Field(ShopVerificationObjectType)

    @staticmethod
    def mutate(root, info, input=None):
        shop = Shop.objects.get(id=input.shop_id)
        success = True

        try:
            shop_verification = ShopVerification.objects.get(shop=shop)
        except ShopVerification.DoesNotExist:
            shop_verification = ShopVerification.objects.create(shop=shop)
        try:
            if input.owner_image:
                shop_verification.owner_image = input.owner_image
            if input.id_front_image:
                shop_verification.id_front_image = input.id_front_image
            if input.id_back_image:
                shop_verification.id_back_image = input.id_back_image

            shop_verification.save()
        except shop_verification.DoesNotExist:
            success = False
            shop_verification = None
        return CreateShopVerification(success=success, shop_verification=shop_verification)


class UpdateShopVerification(graphene.Mutation):
    class Arguments:
        input = UpdateShopVerificationInput()

    success = graphene.Boolean()
    shop_verification = graphene.Field(ShopVerificationObjectType)

    @staticmethod
    def mutate(root, info, input=None):
        success = False
        shop_verification_instance = ShopVerification.objects.get(pk=input.id)
        if shop_verification_instance:
            success = True
            if input.owner_image:
                shop_verification_instance.owner_image = input.owner_image
            if input.id_front_image:
                shop_verification_instance.id_front_image = input.id_front_image
            if input.id_back_image:
                shop_verification_instance.id_back_image = input.id_back_image

            shop_verification_instance.save()
            return UpdateShopVerification(success=success, shop_verification=shop_verification_instance)
        return UpdateShopVerification(success=success, shop_verification=None)


class ShopMutation(graphene.ObjectType):
    create_shop = CreateShop.Field()
    update_shop = UpdateShop.Field()
    delete_shop = DeleteShop.Field()
    create_shop_verification = CreateShopVerification.Field()
    update_shop_verification = UpdateShopVerification.Field()
