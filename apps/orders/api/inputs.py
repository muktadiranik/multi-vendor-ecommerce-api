import graphene
from apps.orders.models import *
from apps.orders.api.schema import *


class CreateOrderInput(graphene.InputObjectType):
    cart_id = graphene.ID(required=False)
    payment_method = graphene.String(required=False)
    is_paid = graphene.Boolean(required=False)
    is_delivered = graphene.Boolean(required=False)
    total_price = graphene.Decimal(required=False)
    delivered_at = graphene.DateTime(required=False)
    returned_at = graphene.DateTime(required=False)
    duration = graphene.Int(required=False)
    address = graphene.String()
    city = graphene.String()
    state = graphene.String()
    zip_code = graphene.String()
    area_code = graphene.String()
    country = graphene.String()
    phone = graphene.String()
    create_time = graphene.DateTime()
    update_time = graphene.DateTime()
    payment_id = graphene.String()
    payment_order_id = graphene.String()
    intent = graphene.String()
    payer_country_code = graphene.String()
    payer_email = graphene.String()
    payer_id = graphene.String()
    payer_name = graphene.String()
    purchase_amount = graphene.Decimal()
    purchase_currency_code = graphene.String()
    purchase_units_reference_id = graphene.String()
    purchase_shipping_address = graphene.JSONString()
    purchase_shipping_name = graphene.String()
    status = graphene.String()


class UpdateOrderInput(graphene.InputObjectType):
    payment_method = graphene.String()
    is_cancelled = graphene.Boolean()
    is_delivered = graphene.Boolean()
    refund_requested = graphene.Boolean()


class OrderItemInput(graphene.InputObjectType):
    product = graphene.ID()
    quantity = graphene.Int()
    price = graphene.Decimal()


class UpdateOrderItemInput(graphene.InputObjectType):
    product = graphene.ID()
    quantity = graphene.Int()
    price = graphene.Decimal()


class CreateShippingAddressInput(graphene.InputObjectType):
    address = graphene.String()
    city = graphene.String()
    state = graphene.String()
    zip_code = graphene.String()
    area_code = graphene.String()
    country = graphene.String()
    phone = graphene.String()


class CreateRefundInput(graphene.InputObjectType):
    order_id = graphene.ID()
    reason = graphene.String()


class UpdateRefundInput(graphene.InputObjectType):
    order_id = graphene.ID()
    reason = graphene.String()
