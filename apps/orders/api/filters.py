from django_filters import FilterSet, CharFilter, NumberFilter, NumericRangeFilter, BooleanFilter
from django.db.models import Q

from apps.orders.models import *


class OrderFilter(FilterSet):
    id = NumberFilter(field_name='id', lookup_expr='exact')
    user_id = NumberFilter(field_name='user', lookup_expr='exact')
    is_paid = BooleanFilter(field_name='is_paid', lookup_expr='exact')
    is_delivered = BooleanFilter(field_name='is_delivered', lookup_expr='exact')

    class Meta:
        model = Order
        fields = "__all__"
        include = ["orderitem_set"]


class OrderItemFilter(FilterSet):
    id = NumberFilter(field_name='id', lookup_expr='exact')
    order_id = NumberFilter(field_name='order', lookup_expr='exact')
    product_id = NumberFilter(field_name='product', lookup_expr='exact')
    shop_id = NumberFilter(field_name='product__shop', lookup_expr='exact')

    class Meta:
        model = OrderItem
        fields = "__all__"
