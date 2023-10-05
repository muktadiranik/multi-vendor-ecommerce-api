from django.contrib import admin
from .models import *


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1
    show_change_link = True
    fields = ('product', 'quantity', 'price', 'created_at')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    can_delete = True


class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['order', 'address', 'city', 'state', 'zip_code', 'area_code', 'country', 'phone']
    search_fields = ['order__user__username']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'rental_number', 'payment_method', 'status', 'is_paid', 'is_delivered',
                    'total_price', 'paid_at', 'delivered_at', 'created_at']
    # list_filter = ['is_paid', 'is_delivered']
    search_fields = ['user__username', 'rental_number']
    inlines = [OrderItemInline]
    readonly_fields = ('rental_number',)


class RefundAdmin(admin.ModelAdmin):
    list_display = ['order', 'reason', 'status', 'created_at']
    list_filter = ['status']
    search_fields = ['order__user__username']


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress, ShippingAddressAdmin)
admin.site.register(PaymentInformation)
admin.site.register(Refund, RefundAdmin)
