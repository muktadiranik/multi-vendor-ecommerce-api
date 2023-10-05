import graphene
from graphene_django.filter import DjangoFilterConnectionField
from apps.products.models import *
from apps.products.api.schema import *



class ProductQuery(graphene.ObjectType):
    all_products = graphene.List(ProductObjectType)
    products = DjangoFilterConnectionField(ProductObjectType)
    get_product_by_id = graphene.Field(ProductObjectType, id=graphene.ID())
    get_products_by_shop_id = graphene.List(ProductObjectType, id=graphene.ID())
    get_products_by_price_range = DjangoFilterConnectionField(ProductObjectType,
                                                              min=graphene.Float(),
                                                              max=graphene.Float())

    get_products_by_price_range_and_currency_id = graphene.List(ProductObjectType,
                                                                min=graphene.Float(),
                                                                max=graphene.Float(),
                                                                id=graphene.ID())
    get_products_by_product_type_id = graphene.List(ProductObjectType, id=graphene.ID())
    get_products_by_price_range_and_product_type_id = graphene.List(ProductObjectType,
                                                                    min=graphene.Float(),
                                                                    max=graphene.Float(),
                                                                    id=graphene.ID())
    get_products_by_price_range_and_product_type_id_and_shop_id = graphene.List(ProductObjectType,
                                                                                min=graphene.Float(),
                                                                                max=graphene.Float(),
                                                                                id=graphene.ID(),
                                                                                shop_id=graphene.ID())
    # product_images = graphene.List(ProductImageObjectType)
    # get_product_image_by_id = graphene.Field(ProductImageObjectType, id=graphene.ID())
    # get_product_images_by_product_id = graphene.Field(ProductImageObjectType, id=graphene.ID())
    products_rates = graphene.List(ProductRateObjectType)
    products_sizes = graphene.List(ProductSizeObjectType)
    products_options = graphene.List(ProductOptionObjectType)

    product_reviews = graphene.List(ProductReviewObjectType)
    get_product_reviews_by_product_id = graphene.List(ProductReviewObjectType, id=graphene.ID())
    product_demurrages = graphene.List(ProductDamageObjectType)
    get_product_demurrages_by_product_id = graphene.List(ProductDamageObjectType, id=graphene.ID())
    get_product_reviews_by_shop_id = graphene.List(ProductReviewObjectType, id=graphene.ID())

    def resolve_products(self, info, **kwargs):
        return Product.objects.\
            prefetch_related("productrate_set").\
            prefetch_related("productoption_set").\
            prefetch_related("productdeposit_set").\
            prefetch_related("orderitem_set").all()

    def resolve_get_product_by_id(self, info, id):
        return Product.objects.\
            prefetch_related("productrate_set").\
            prefetch_related("productdeposit_set").\
            prefetch_related("productoption_set").get(pk=id)

    def resolve_get_products_by_shop_id(self, info, id):
        return Product.objects.\
            prefetch_related("productrate_set").\
            prefetch_related("productdeposit_set").\
            prefetch_related("productoption_set").filter(shop=id)

    def resolve_get_products_by_price_range(self, info, min=None, max=None):
        product_id_range = ProductRate.objects.all().values_list('product', flat=True)
        if min:
            product_id_range = product_id_range.filter(rate__gte=min).values_list('product', flat=True)
        if max:
            product_id_range = product_id_range.filter(rate__lte=max).values_list('product', flat=True)

        return Product.objects.\
            prefetch_related("productrate_set").\
            prefetch_related("productdeposit_set").\
            prefetch_related("productoption_set").filter(id__in=product_id_range)

    def resolve_get_products_by_price_range_and_currency_id(self, info, id=None, min=None, max=None):
        product_id_range = ProductRate.objects.all().values_list('product', flat=True)
        if min:
            product_id_range = product_id_range.filter(rate__gte=min).values_list('product', flat=True)
        if max:
            product_id_range = product_id_range.filter(rate__lte=max).values_list('product', flat=True)

        if id:
            product_id_range = product_id_range.filter(currency=id).values_list('product', flat=True)

        return Product.objects.\
            prefetch_related("productrate_set").\
            prefetch_related("productdeposit_set").\
            prefetch_related("productoption_set").filter(id__in=product_id_range)

    def resolve_get_products_by_product_type_id(self, info, id):
        return Product.objects.\
            prefetch_related("productrate_set").\
            prefetch_related("productdeposit_set").\
            prefetch_related("productoption_set").filter(product_type=id)

    def resolve_get_products_by_price_range_and_product_type_id(self, info, id=None, min=None, max=None):
        product_id_range = ProductRate.objects.all().values_list('product', flat=True)
        if min:
            product_id_range = product_id_range.filter(rate__gte=min).values_list('product', flat=True)
        if max:
            product_id_range = product_id_range.filter(rate__lte=max).values_list('product', flat=True)

        queryset = Product.objects.\
            prefetch_related("productrate_set").\
            prefetch_related("productdeposit_set").\
            prefetch_related("productoption_set").all()

        if id:
            queryset = queryset.filter(product_type=id)
        if min:
            queryset = queryset.filter(id__in=product_id_range)
        if max:
            queryset = queryset.filter(id__in=product_id_range)

        return queryset

    def resolve_get_products_by_price_range_and_product_type_id_and_shop_id(self, info, id=None, shop_id=None, min=None, max=None):
        product_id_range = ProductRate.objects.all().values_list('product', flat=True)
        if min:
            product_id_range = product_id_range.filter(rate__gte=min).values_list('product', flat=True)
        if max:
            product_id_range = product_id_range.filter(rate__lte=max).values_list('product', flat=True)

        queryset = Product.objects.\
            prefetch_related("productrate_set").\
            prefetch_related("productdeposit_set").\
            prefetch_related("productoption_set").all()

        if product_id_range:
            queryset = queryset.filter(id__in=product_id_range)
        if id:
            queryset = queryset.filter(product_type=id)
        if shop_id:
            queryset = queryset.filter(shop=shop_id)

        return queryset

    def resolve_get_products_by_price_range_and_shop_id(self, info, min=None, max=None, id=None):
        product_id_range = ProductRate.objects.all().values_list('product', flat=True)
        if min:
            product_id_range = product_id_range.filter(rate__gte=min).values_list('product', flat=True)
        if max:
            product_id_range = product_id_range.filter(rate__lte=max).values_list('product', flat=True)

        queryset = Product.objects.\
            prefetch_related("productrate_set").\
            prefetch_related("productdeposit_set").\
            prefetch_related("productoption_set").all()

        if product_id_range:
            queryset = queryset.filter(id__in=product_id_range)
        if id:
            queryset = queryset.filter(shop=id)

        return queryset

    # def resolve_products_images(self, info, **kwargs):
    #     return ProductImage.objects.all()

    # def resolve_get_product_image_by_id(self, info, id):
    #     return ProductImage.objects.get(pk=id)

    # def resolve_get_product_images_by_product_id(self, info, id):
    #     return ProductImage.objects.filter(product=id)

    def resolve_products_rates(self, info, **kwargs):
        return ProductRate.objects.all()

    def resolve_products_sizes(self, info, **kwargs):
        return ProductSize.objects.all()

    def resolve_products_options(self, info, **kwargs):
        return ProductOption.objects.all()

    def resolve_product_reviews(self, info, **kwargs):
        return ProductReview.objects.all()

    def resolve_get_product_reviews_by_product_id(self, info, id):
        return ProductReview.objects.filter(product=id).order_by('-created_at')

    def resolve_product_demurrages(self, info, **kwargs):
        return ProductDamage.objects.all()

    def resolve_get_product_demurrages_by_product_id(self, info, id):
        return ProductDamage.objects.filter(product=id)

    def resolve_get_product_reviews_by_shop_id(self, info, id):
        return ProductReview.objects.filter(product__shop=id).order_by('-created_at')

    def resolve_all_products(self, info, **kwargs):
        return Product.objects.all()


product_schema_query = graphene.Schema(query=ProductQuery)
