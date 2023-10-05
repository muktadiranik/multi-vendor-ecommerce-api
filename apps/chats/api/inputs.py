import graphene
from apps.chats.models import *
from apps.chats.api.schema import *


class CreateConnectionInput(graphene.InputObjectType):
    sender = graphene.ID()
    receiver = graphene.ID()
