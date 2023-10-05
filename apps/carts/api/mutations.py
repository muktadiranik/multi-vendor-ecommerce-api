import graphene
from apps.carts.models import *
from apps.products.models import *
from apps.users.models import *
from apps.carts.api.schema import *


class AddToCart(graphene.Mutation):
    cart_item = graphene.Field(CartItemObjectType)
    cart = graphene.Field(CartObjectType)

    class Arguments:
        user_id = graphene.ID()
        product_id = graphene.ID()
        quantity = graphene.Int()

    def mutate(self, info, user_id, product_id, quantity):
        user = User.objects.get(id=user_id)
        try:
            cart = Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(user=user)

        try:
            cart_item = CartItem.objects.get(
                cart=cart, product=Product.objects.get(id=product_id))
            cart_item.quantity += quantity
            cart_item.save()
        except CartItem.DoesNotExist:
            cart_item = CartItem.objects.create(
                cart=cart,
                product=Product.objects.get(id=product_id),
                quantity=quantity,
                price=ProductRate.objects.filter(product=product_id).first().rate)
        return AddToCart(cart=cart, cart_item=cart_item)


class RemoveFromCart(graphene.Mutation):
    cart_item = graphene.Field(CartItemObjectType)
    cart = graphene.Field(CartObjectType)

    class Arguments:
        user_id = graphene.ID()
        product_id = graphene.ID()
        quantity = graphene.Int()

    def mutate(self, info, user_id, product_id, quantity):
        user = User.objects.get(id=user_id)
        product = Product.objects.get(id=product_id)
        cart = Cart.objects.get(user=user)
        cart_item = CartItem.objects.get(cart=cart, product=product)
        cart_item.quantity -= quantity
        if cart_item.quantity == 0:
            cart_item.delete()
            cart_item = None
        else:
            cart_item.save()
        return RemoveFromCart(cart=cart, cart_item=cart_item)


class CartMutation(graphene.ObjectType):
    add_to_cart = AddToCart.Field()
    remove_from_cart = RemoveFromCart.Field()
