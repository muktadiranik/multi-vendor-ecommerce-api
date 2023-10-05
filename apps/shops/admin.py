from django.contrib import admin
from .models import *


class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'rating', 'total_reviews', 'is_verified', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'phone', 'email', 'website')
    readonly_fields = ('created_at', 'updated_at', 'rating', 'total_reviews', 'is_verified',)
    ordering = ('-created_at',)


class ShopVerificationAdmin(admin.ModelAdmin):
    list_display = ('shop', 'status', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('shop__name', 'shop__phone', 'shop__email', 'shop__website')
    ordering = ('-created_at',)


class PickUpLocationAdmin(admin.ModelAdmin):
    list_display = ('shop', 'country', 'created_at')
    list_filter = ('created_at',)


admin.site.register(Shop, ShopAdmin)
admin.site.register(PickUpLocation, PickUpLocationAdmin)
admin.site.register(ShopVerification, ShopVerificationAdmin)
