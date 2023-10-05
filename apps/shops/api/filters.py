from django_filters import (FilterSet,
                            CharFilter,
                            NumberFilter,
                            NumericRangeFilter,

                            )
from apps.shops.models import *


class ShopFilter(FilterSet):
    id = CharFilter(field_name='id', lookup_expr='exact')
    owner_id = CharFilter(field_name='owner', lookup_expr='exact')
    street = CharFilter(field_name='street', lookup_expr='icontains')
    city = CharFilter(field_name='city', lookup_expr='icontains')
    state = CharFilter(field_name='state', lookup_expr='icontains')
    zip_code = CharFilter(field_name='zip_code', lookup_expr='icontains')
    area_code = CharFilter(field_name='area_code', lookup_expr='icontains')
    country = CharFilter(field_name='country', lookup_expr='icontains')
    phone = CharFilter(field_name='phone', lookup_expr='icontains')

    lat_min = NumberFilter(field_name='latitude', lookup_expr='gte')
    lat_max = NumberFilter(field_name='latitude', lookup_expr='lte')

    lon_min = NumberFilter(field_name='longitude', lookup_expr='gte')
    lon_max = NumberFilter(field_name='longitude', lookup_expr='lte')

    latitude = NumericRangeFilter(field_name='latitude')
    longitude = NumericRangeFilter(field_name='longitude')
    website = CharFilter(field_name='website', lookup_expr='icontains')
    email = CharFilter(field_name='email', lookup_expr='icontains')
    description = CharFilter(field_name='description', lookup_expr='icontains')
    opening_time = CharFilter(field_name='opening_time', lookup_expr='icontains')
    closing_time = CharFilter(field_name='closing_time', lookup_expr='icontains')
    shop_image = CharFilter(field_name='shop_image', lookup_expr='icontains')
    shop_cover = CharFilter(field_name='shop_cover', lookup_expr='icontains')

    class Meta:
        model = Shop
        fields = "__all__"
        include = ["product_set",
                   "pickuplocation_set",]
