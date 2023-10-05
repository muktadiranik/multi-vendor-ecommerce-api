import graphene
from django_filters import FilterSet, CharFilter
from apps.carts.models import *


class CartFilter(FilterSet):
    id = CharFilter(field_name='id', lookup_expr='exact')
    user_id = CharFilter(field_name='user', lookup_expr='exact')

    class Meta:
        model = Cart
        fields = "__all__"
        include = ["cartitem_set"]
        interfaces = (graphene.relay.Node,)


class CartItemFilter(FilterSet):
    id = CharFilter(field_name='id', lookup_expr='exact')
    cart_id = CharFilter(field_name='cart', lookup_expr='exact')
    product_id = CharFilter(field_name='product', lookup_expr='exact')

    class Meta:
        model = CartItem
        fields = "__all__"
        interfaces = (graphene.relay.Node,)
