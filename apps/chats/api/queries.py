import graphene
from graphene_django.filter import DjangoFilterConnectionField
from apps.chats.models import *
from apps.chats.api.schema import *


class ChatQuery(graphene.ObjectType):
    connections = DjangoFilterConnectionField(ConnectionObjectType)
    conversations = DjangoFilterConnectionField(ConversationObjectType)

    def resolve_connections(self, info, **kwargs):
        return Connection.objects.all()

    def resolve_conversations(self, info, **kwargs):
        return Conversation.objects.all()


chat_schema_query = graphene.Schema(query=ChatQuery)
