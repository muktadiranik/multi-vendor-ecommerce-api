import graphene
from graphene_django.filter import DjangoFilterConnectionField
from apps.orders.models import *
from apps.orders.api.schema import *
from apps.orders.api.inputs import *
from apps.products.models import *
from apps.products.api.schema import *


class OrderQuery(graphene.ObjectType):
    orders = DjangoFilterConnectionField(OrderType)
    order = graphene.Field(OrderType, id=graphene.ID(required=True))
    latest_order = graphene.List(OrderItemType)
    refunds = graphene.List(RefundObjectType)
    order_item_by_shop_id = graphene.List(OrderType, shop_id=graphene.ID(required=True))
    order_item_by_order_id = graphene.List(OrderItemType, order_id=graphene.ID(required=True))
    order_by_user_id = graphene.List(OrderType, user_id=graphene.ID(required=True))
    order_by_shop_id = graphene.List(OrderType, shop_id=graphene.ID(required=True))
    refund_by_user_id = graphene.List(RefundObjectType, user_id=graphene.ID(required=True))
    order_items = DjangoFilterConnectionField(OrderItemType)
    payment_informations = graphene.List(PaymentInformationObjectType)

    def resolve_orders(self, info, **kwargs):
        return Order.objects.all()

    def resolve_order(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Order.objects.get(pk=id)
        return None

    def resolve_latest_order(self, info, **kwargs):
        return OrderItem.objects.all().order_by('-id')[0:3]

    def resolve_order_by_user_id(self, info, **kwargs):
        user_id = kwargs.get('user_id')
        if user_id is not None:
            return Order.objects.filter(user_id=user_id)
        return None

    def resolve_order_item_by_shop_id(self, info, **kwargs):
        shop_id = kwargs.get('shop_id')
        if shop_id is not None:
            return Order.objects.filter(product__shop_id=shop_id)
        return None

    def resolve_order_item_by_order_id(self, info, **kwargs):
        order_id = kwargs.get('order_id')
        if order_id is not None:
            return OrderItem.objects.filter(order_id=order_id)
        return None

    def resolve_refunds(self, info, **kwargs):
        return Refund.objects.all()

    def resolve_refund_by_user_id(self, info, **kwargs):
        user_id = kwargs.get('user_id')
        if user_id is not None:
            return Refund.objects.filter(order__user_id=user_id)
        return None

    def resolve_order_items(self, info, **kwargs):
        return OrderItem.objects.all()

    def resolve_payment_informations(self, info, **kwargs):
        return PaymentInformation.objects.all()


order_schema_query = graphene.Schema(query=OrderQuery)
