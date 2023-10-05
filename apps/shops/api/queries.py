import graphene
from graphene_django.filter import DjangoFilterConnectionField
from apps.shops.models import *
from apps.shops.api.schema import *


class ShopQuery(graphene.ObjectType):
    shops = DjangoFilterConnectionField(ShopObjectType)
    shop_varifications = graphene.List(ShopVerificationObjectType)
    pick_up_locations = graphene.List(PickupLocationObjectType)

    def resolve_shops(self, info, **kwargs):
        return Shop.objects.all().prefetch_related("product_set").\
            prefetch_related("pickuplocation_set")

    def resolve_shop_varifications(self, info, **kwargs):
        return ShopVerification.objects.all()

    def resolve_pick_up_locations(self, info, **kwargs):
        return PickUpLocation.objects.all()


shop_schema_query = graphene.Schema(query=ShopQuery)
