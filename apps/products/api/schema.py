import graphene
from graphene_django import DjangoObjectType
from apps.products.models import *
from apps.products.api.filters import *
from graphene import String
from dateutil.parser import parse


class ProductObjectType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)

    # description = String()

    # def resolve_description(self, info):
    #     if self.description:
    #         return self.description.html

    created_at = graphene.String()
    updated_at = graphene.String()

    def resolve_created_at(self, info):
        if self.created_at:
            return parse(str(self.created_at)).strftime("%b %d, %Y, %I:%M %p")

    def resolve_updated_at(self, info):
        if self.updated_at:
            return parse(str(self.updated_at)).strftime("%b %d, %Y, %I:%M %p")

    class Meta:
        model = Product
        fields = "__all__"
        include = ["productrate_set",
                   "productoption_set",
                   "productdeposit_set",
                   "orderitem_set"]
        filterset_class = ProductFilter
        interfaces = (graphene.relay.Node,)

    def resolve_image(self, info):
        if self.image:
            self.image = info.context.build_absolute_uri(self.image.url)
        return self.image


# class ProductImageObjectType(DjangoObjectType):
#     class Meta:
#         model = ProductImage
#         fields = "__all__"

#     def resolve_image(self, info):
#         if self.image:
#             self.image = info.context.build_absolute_uri(self.image.url)
#         return self.image


class ProductRateObjectType(DjangoObjectType):
    class Meta:
        model = ProductRate
        fields = "__all__"


class ProductSizeObjectType(DjangoObjectType):
    class Meta:
        model = ProductSize
        fields = "__all__"


class ProductOptionObjectType(DjangoObjectType):
    class Meta:
        model = ProductOption
        fields = "__all__"


class ProductReviewObjectType(DjangoObjectType):

    created_at = graphene.String()
    updated_at = graphene.String()

    def resolve_created_at(self, info):
        if self.created_at:
            return parse(str(self.created_at)).strftime("%b %d, %Y, %I:%M %p")

    def resolve_updated_at(self, info):
        if self.updated_at:
            return parse(str(self.updated_at)).strftime("%b %d, %Y, %I:%M %p")

    def resolve_user_image(self, info):
        if self.user_image:
            self.user_image = info.context.build_absolute_uri(self.user_image.url)
        return self.user_image

    class Meta:
        model = ProductReview
        fields = "__all__"


class ProductDamageObjectType(DjangoObjectType):
    class Meta:
        model = ProductDamage
        fields = "__all__"


class ProductDepositObjectType(DjangoObjectType):
    class Meta:
        model = ProductDeposit
        fields = "__all__"
