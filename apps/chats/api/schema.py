import graphene
from graphene_django import DjangoObjectType
from apps.chats.models import *
from apps.chats.api.filters import *
from dateutil.parser import parse


class ConnectionObjectType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)

    created_at = graphene.String()
    updated_at = graphene.String()

    def resolve_created_at(self, info, **kwargs):
        if self.created_at:
            return parse(str(self.created_at)).strftime("%b %d, %Y, %I:%M %p")

    def resolve_updated_at(self, info, **kwargs):
        if self.updated_at:
            return parse(str(self.updated_at)).strftime("%b %d, %Y, %I:%M %p")

    class Meta:
        model = Connection
        fields = "__all__"
        interfaces = (graphene.relay.Node,)
        filterset_class = ConnectionFilter


class ConversationObjectType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)

    created_at = graphene.String()
    updated_at = graphene.String()

    def resolve_created_at(self, info, **kwargs):
        if self.created_at:
            return parse(str(self.created_at)).strftime("%b %d, %Y, %I:%M %p")

    def resolve_updated_at(self, info, **kwargs):
        if self.updated_at:
            return parse(str(self.updated_at)).strftime("%b %d, %Y, %I:%M %p")

    class Meta:
        model = Conversation
        fields = "__all__"
        interfaces = (graphene.relay.Node,)
        filterset_class = ConversationFilter
