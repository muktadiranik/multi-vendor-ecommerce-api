import graphene
from django.db import transaction
from apps.orders.models import *
from apps.orders.api.schema import *
from apps.orders.api.inputs import *
from apps.products.models import *
from apps.products.api.schema import *
from apps.carts.models import *
from apps.carts.api.schema import *


class CreateOrder(graphene.Mutation):
    class Arguments:
        input = CreateOrderInput()

    success = graphene.Boolean()
    order = graphene.Field(OrderType)

    @staticmethod
    def mutate(root, info, input=None):
        success = True
        with transaction.atomic():
            order_instance = Order.objects.create()
            cart = Cart.objects.get(id=input.cart_id)
            order_instance.user = User.objects.get(id=cart.user.id)
            if input.payment_method:
                order_instance.payment_method = input.payment_method
            if input.is_paid:
                order_instance.is_paid = input.is_paid
            if input.total_price:
                order_instance.total_price = input.total_price
            if input.is_delivered:
                order_instance.is_delivered = input.is_delivered
            if input.total_price:
                order_instance.total_price = input.total_price
            if input.delivered_at:
                order_instance.delivered_at = input.delivered_at
            if input.returned_at:
                order_instance.returned_at = input.returned_at
            if input.duration:
                order_instance.duration = input.duration
            order_instance.save()
            cart_items = CartItem.objects.filter(cart=cart)
            for i in cart_items:
                product = Product.objects.get(id=i.product.id)
                product.stock -= i.quantity
                product.save()
            order_items = [OrderItem(
                product=cart_item.product,
                quantity=cart_item.quantity,
                price=cart_item.price,
                order=order_instance
            ) for cart_item in cart_items]
            cart_items.delete()
            OrderItem.objects.bulk_create(order_items)
            shipping_address_instance = ShippingAddress.objects.create(order=order_instance)
            if input.address:
                shipping_address_instance.address = input.address
            if input.city:
                shipping_address_instance.city = input.city
            if input.state:
                shipping_address_instance.state = input.state
            if input.zip_code:
                shipping_address_instance.zip_code = input.zip_code
            if input.area_code:
                shipping_address_instance.area_code = input.area_code
            if input.country:
                shipping_address_instance.country = input.country
            if input.phone:
                shipping_address_instance.phone = input.phone
            shipping_address_instance.save()
            payment_information_instance = PaymentInformation.objects.create(order=order_instance)
            if input.create_time:
                payment_information_instance.create_time = input.create_time
            if input.update_time:
                payment_information_instance.update_time = input.update_time
            if input.payment_id:
                payment_information_instance.payment_id = input.payment_id
            if input.payment_order_id:
                payment_information_instance.payment_order_id = input.payment_order_id
            if input.intent:
                payment_information_instance.intent = input.intent
            if input.payer_country_code:
                payment_information_instance.payer_country_code = input.payer_country_code
            if input.payer_email:
                payment_information_instance.payer_email = input.payer_email
            if input.payer_id:
                payment_information_instance.payer_id = input.payer_id
            if input.payer_name:
                payment_information_instance.payer_name = input.payer_name
            if input.purchase_amount:
                payment_information_instance.purchase_amount = input.purchase_amount
            if input.purchase_currency_code:
                payment_information_instance.purchase_currency_code = input.purchase_currency_code
            if input.purchase_units_reference_id:
                payment_information_instance.purchase_units_reference_id = input.purchase_units_reference_id
            if input.purchase_shipping_address:
                payment_information_instance.purchase_shipping_address = input.purchase_shipping_address
            if input.purchase_shipping_name:
                payment_information_instance.purchase_shipping_name = input.purchase_shipping_name
            if input.status:
                payment_information_instance.status = input.status
            payment_information_instance.save()
        return CreateOrder(success=success, order=order_instance)


class UpdateOrder(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = UpdateOrderInput()
    success = graphene.Boolean()
    order = graphene.Field(OrderType)

    @staticmethod
    def mutate(root, info, id, input=None):
        success = False
        order_instance = Order.objects.get(pk=id)
        if order_instance:
            success = True
            if input.payment_method:
                order_instance.payment_method = input.payment_method
            if input.is_cancelled == False:
                order_instance.is_cancelled = False
            elif input.is_cancelled == True:
                order_instance.is_cancelled = True
            if input.refund_requested == False:
                order_instance.refund_requested = False
            elif input.refund_requested == True:
                order_instance.refund_requested = True
            if input.is_delivered == False:
                order_instance.is_delivered = False
            elif input.is_delivered == True:
                order_instance.is_delivered = True

            order_instance.save()
            return UpdateOrder(success=success, order=order_instance)
        return UpdateOrder(success=success, order=None)


class DeleteOrder(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()
    order = graphene.Field(OrderType)

    @staticmethod
    def mutate(root, info, id):
        success = False
        order_instance = Order.objects.get(pk=id)
        if order_instance:
            success = True
            order_instance.delete()
        return DeleteOrder(success=success, order=order_instance)


class CreateRefund(graphene.Mutation):
    class Arguments:
        input = CreateRefundInput()
    success = graphene.Boolean()
    refund = graphene.Field(RefundObjectType)

    def mutate(self, info, input=None):

        refund_instance = Refund.objects.create(
            order=Order.objects.get(pk=input.order_id),
            reason=input.reason,
        )
        success = True

        return CreateRefund(success=success, refund=refund_instance)


class DeleteRefund(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()
    refund = graphene.Field(RefundObjectType)

    @staticmethod
    def mutate(root, info, id):
        success = False
        refund_instance = Refund.objects.get(pk=id)
        if refund_instance:
            success = True
            refund_instance.delete()
        return DeleteRefund(success=success, refund=refund_instance)


class OrderMutation(graphene.ObjectType):
    create_order = CreateOrder.Field()
    update_order = UpdateOrder.Field()
    delete_order = DeleteOrder.Field()
    create_refund = CreateRefund.Field()
    delete_refund = DeleteRefund.Field()
