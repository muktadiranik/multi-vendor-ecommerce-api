from django.contrib import admin
from .models import *


class CartproductInline(admin.TabularInline):
    model = CartItem
    extra = 1
    show_change_link = True
    fields = ('product', 'quantity', 'created_at')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    can_delete = True


class CartAdmin(admin.ModelAdmin):
    inlines = [CartproductInline]


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem)
