from django.contrib import admin
from .models import *


# class ProductImageInline(admin.TabularInline):
#     model = ProductImage
#     extra = 1


class ProductRateInline(admin.TabularInline):
    model = ProductRate
    extra = 1


class ProductOptionInline(admin.TabularInline):
    model = ProductOption
    extra = 1


# class ProductConditionInline(admin.TabularInline):
#     model = ProductCondition
#     extra = 1


class ProductDepositInline(admin.TabularInline):
    model = ProductDeposit
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'shop', 'stock', 'rating', 'total_reviews', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('rating', 'total_reviews', )
    search_fields = ('brand', 'model', 'shop__name',)
    ordering = ('-created_at',)
    inlines = [ProductRateInline, ProductOptionInline, ProductDepositInline,]


# class ProductStockAdmin(admin.ModelAdmin):
#     list_display = ('product', 'stock', 'created_at',)
#     list_filter = ('created_at', 'updated_at')
#     search_fields = ('product__model',)
#     ordering = ('-created_at',)


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'review', 'rating', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('product', 'user',)
    ordering = ('-created_at',)


class ProductDemurrageAdmin(admin.ModelAdmin):
    list_display = ('product', 'created_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('product__model',)
    ordering = ('-created_at',)


# class ProductImageAdmin(admin.ModelAdmin):
#     list_display = ('product', 'image', 'is_default')
#     search_fields = ('product__model',)
#     ordering = ('-created_at',)


# admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(ProductSize)
admin.site.register(ProductOption)
# admin.site.register(ProductCondition)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(ProductDamage, ProductDemurrageAdmin)
