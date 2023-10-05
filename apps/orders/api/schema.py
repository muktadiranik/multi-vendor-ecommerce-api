import graphene
from graphene_django import DjangoObjectType
from apps.orders.models import *
from . filters import *
from dateutil.parser import parse


class OrderType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)

    paid_at = graphene.String()
    delivered_at = graphene.String()
    returned_at = graphene.String()
    created_at = graphene.String()

    def resolve_created_at(self, info):
        if self.created_at:
            return parse(str(self.created_at)).strftime("%b %d, %Y  %I:%M %p")

    def resolve_paid_at(self, info):
        if self.paid_at:
            return parse(str(self.paid_at)).strftime("%b %d, %Y, %I:%M %p")

    def resolve_delivered_at(self, info):
        if self.delivered_at:
            return parse(str(self.delivered_at)).strftime("%b %d, %Y")

    def resolve_returned_at(self, info):
        if self.returned_at:
            return parse(str(self.returned_at)).strftime("%b %d, %Y")

    class Meta:
        model = Order
        fields = "__all__"
        include = ["orderitem_set", "paymentinformationSet"]
        filterset_class = OrderFilter
        interfaces = (graphene.relay.Node,)


class OrderItemType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)

    created_at = graphene.String()

    def resolve_created_at(self, info):
        if self.created_at:
            return parse(str(self.created_at)).strftime("%b %d, %Y, %I:%M %p")

    class Meta:
        model = OrderItem
        fields = "__all__"
        filterset_class = OrderItemFilter
        interfaces = (graphene.relay.Node,)


class RefundObjectType(DjangoObjectType):

    created_at = graphene.String()

    def resolve_created_at(self, info):
        if self.created_at:
            return parse(str(self.created_at)).strftime("%b %d, %Y, %I:%M %p")

    class Meta:
        model = Refund
        fields = ("id", "order", "reason", "status", "created_at")


class PaymentInformationObjectType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)

    class Meta:
        model = PaymentInformation
        fields = "__all__"
        interfaces = (graphene.relay.Node,)
