from django_filters import (FilterSet,
                            CharFilter,
                            NumberFilter,
                            NumericRangeFilter,
                            DateFilter,
                            )
from django.db.models import Q
from apps.products.models import *
from datetime import datetime, timedelta


class ProductFilter(FilterSet):
    id = CharFilter(field_name='id', lookup_expr='exact')
    model = CharFilter(field_name='model', lookup_expr='icontains')
    brand = CharFilter(field_name='brand', lookup_expr='icontains')
    description = CharFilter(field_name='description', lookup_expr='icontains')
    stock = NumberFilter(field_name='stock', lookup_expr='exact')
    shop_id = NumberFilter(field_name='shop', lookup_expr='exact')
    shop_location = CharFilter(method='filter_shop_location')
    image = CharFilter(field_name='image', lookup_expr='icontains')
    date = DateFilter(method='filter_date')
    riders = NumberFilter(method='filter_riders')
    size = CharFilter(field_name='size', lookup_expr='exact')

    lat_min = NumberFilter(field_name='shop__latitude', lookup_expr='gte')
    lat_max = NumberFilter(field_name='shop__latitude', lookup_expr='lte')

    lon_min = NumberFilter(field_name='shop__longitude', lookup_expr='gte')
    lon_max = NumberFilter(field_name='shop__longitude', lookup_expr='lte')

    latitude = NumericRangeFilter(field_name='shop__latitude')
    longitude = NumericRangeFilter(field_name='shop__longitude')

    product_type_id = CharFilter(field_name='product_type', lookup_expr='exact')
    product_rate_type_id = CharFilter(field_name='productrate__rate_type', lookup_expr='exact')
    product_rate_type_name = CharFilter(method='filter_product_rate_type_name')
    product_rate_min = NumberFilter(field_name='productrate__rate', lookup_expr='gte')
    product_rate_max = NumberFilter(field_name='productrate__rate', lookup_expr='lte')
    product_rate_range = NumericRangeFilter(field_name='productrate__rate')
    product_option_id = NumberFilter(field_name='productoption__id', lookup_expr='exact')

    class Meta:
        model = Product
        fields = "__all__"
        include = ["productrate_set",
                   "productoption_set"]

    def filter_shop_location(self, queryset, name, value):
        return queryset.filter(Q(shop__name__icontains=value)
                               |
                               Q(shop__street__icontains=value)
                               |
                               Q(shop__city__icontains=value)
                               |
                               Q(shop__state__icontains=value)
                               |
                               Q(shop__zip_code__icontains=value)
                               |
                               Q(shop__area_code__icontains=value)
                               |
                               Q(shop__country__icontains=value))

    def filter_date(self, queryset, name, value):
        date_range = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')

        return queryset.filter(created_at__date__gte=date_range).filter(is_available=True).distinct()

    def filter_riders(self, queryset, name, value):
        value = int(value)
        stock = queryset.filter(stock__gte=value)
        if value > 0:
            return stock
        else:
            return queryset

    def filter_product_rate_type_name(self, queryset, name, value):
        return queryset.filter(Q(productrate__rate_type__name__icontains=value)).distinct()
