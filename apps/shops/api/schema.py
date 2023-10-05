import graphene
from graphene_django import DjangoObjectType
from apps.shops.models import *
from apps.shops.api.filters import *
from dateutil.parser import parse


class ShopObjectType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)

    terms_and_condition = graphene.String()
    created_at = graphene.String()
    updated_at = graphene.String()
    opening_time = graphene.String()
    closing_time = graphene.String()

    def resolve_terms_and_condition(self, info):
        if self.terms_and_condition:
            return self.terms_and_condition.html

    def resolve_created_at(self, info):
        if self.created_at:
            return parse(str(self.created_at)).strftime("%b %d, %Y")

    def resolve_updated_at(self, info):
        if self.updated_at:
            return parse(str(self.updated_at)).strftime("%b %d, %Y")

    def resolve_opening_time(self, info):
        if self.opening_time:
            return self.opening_time.strftime("%I:%M %p")

    def resolve_closing_time(self, info):
        if self.closing_time:
            return self.closing_time.strftime("%I:%M %p")

    class Meta:
        model = Shop
        fields = "__all__"
        include = ["product_set",
                   'pickuplocation_set',
                   'shopverification_set'
                   ]
        filterset_class = ShopFilter
        interfaces = (graphene.relay.Node,)

    def resolve_shop_image(self, info):
        if self.shop_image:
            self.shop_image = info.context.build_absolute_uri(self.shop_image.url)
        return self.shop_image

    def resolve_shop_cover(self, info):
        if self.shop_cover:
            self.shop_cover = info.context.build_absolute_uri(self.shop_cover.url)
        return self.shop_cover


class PickupLocationObjectType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)

    class Meta:
        model = PickUpLocation
        fields = "__all__"
        interfaces = (graphene.relay.Node,)


class ShopVerificationObjectType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    created_at = graphene.String()
    updated_at = graphene.String()

    def resolve_created_at(self, info):
        if self.created_at:
            return parse(str(self.created_at)).strftime("%b %d, %Y")

    def resolve_updated_at(self, info):
        if self.updated_at:
            return parse(str(self.updated_at)).strftime("%b %d, %Y")

    def resolve_owner_image(self, info):
        if self.owner_image:
            self.owner_image = info.context.build_absolute_uri(self.owner_image.url)
        return self.owner_image

    def resolve_id_front_image(self, info):
        if self.id_front_image:
            self.id_front_image = info.context.build_absolute_uri(self.id_front_image.url)
        return self.id_front_image

    def resolve_id_back_image(self, info):
        if self.id_back_image:
            self.id_back_image = info.context.build_absolute_uri(self.id_back_image.url)
        return self.id_back_image

    class Meta:
        model = ShopVerification
        fields = "__all__"
