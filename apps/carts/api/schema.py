from graphene_django import DjangoObjectType
from apps.carts.models import *
from apps.carts.api.filters import *
from dateutil.parser import parse


class CartObjectType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    created_at = graphene.String()
    updated_at = graphene.String()

    def resolve_created_at(self, info):
        if self.created_at:
            return parse(str(self.created_at)).strftime("%b %d, %Y, %I:%M %p")

    def resolve_updated_at(self, info):
        if self.updated_at:
            return parse(str(self.updated_at)).strftime("%b %d, %Y, %I:%M %p")

    class Meta:
        model = Cart
        fields = "__all__"
        filterset_class = CartFilter
        interfaces = (graphene.relay.Node,)


class CartItemObjectType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    created_at = graphene.String()

    def resolve_created_at(self, info):
        if self.created_at:
            return parse(str(self.created_at)).strftime("%b %d, %Y, %I:%M %p")

    class Meta:
        model = CartItem
        fields = "__all__"
        filterset_class = CartItemFilter
        interfaces = (graphene.relay.Node,)
