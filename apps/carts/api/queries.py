import graphene
from graphene_django.filter import DjangoFilterConnectionField
from apps.carts.models import *
from apps.carts.api.schema import *


class CartsQuery(graphene.ObjectType):
    carts = DjangoFilterConnectionField(CartObjectType)
    cart_items = DjangoFilterConnectionField(CartItemObjectType)

    def resolve_all_carts(self, info, **kwargs):
        return Cart.objects.all()

    def resolve_cart_items(self, info, **kwargs):
        return CartItem.objects.all()


cart_schema_query = graphene.Schema(query=CartsQuery)
