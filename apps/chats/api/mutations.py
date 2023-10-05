import graphene
from django.contrib.auth import get_user_model
from django.db.models import Q
from apps.chats.models import *
from apps.chats.api.schema import *
from apps.chats.api.inputs import *

User = get_user_model()


class CreateConnection(graphene.Mutation):
    class Arguments:
        input = CreateConnectionInput(required=True)

    success = graphene.Boolean()
    connection = graphene.Field(ConnectionObjectType)

    @staticmethod
    def mutate(root, info, input=None):
        success = True
        connection_instance = None
        sender = User.objects.get(pk=input.sender)
        receiver = User.objects.get(pk=input.receiver)
        try:
            criterion_1 = Q(sender=input.sender)
            criterion_2 = Q(receiver=input.receiver)
            criterion_3 = Q(sender=input.receiver)
            criterion_4 = Q(receiver=input.sender)
            connection_count = Connection.objects.filter(
                (criterion_1 & criterion_2) | (criterion_3 & criterion_4)).count()
            if connection_count > 0:
                connection = Connection.objects.filter(
                    (criterion_1 & criterion_2) | (criterion_3 & criterion_4))
                connection_instance = connection.first()
                return CreateConnection(connection=connection_instance)
            elif connection_count == 0:
                connection_instance = Connection(
                    sender=sender,
                    receiver=receiver
                )
                connection_instance.save()
                return CreateConnection(success=success, connection=connection_instance)
        except:
            connection_instance = Connection(
                sender=sender,
                receiver=receiver,
            )
            connection_instance.save()
            return CreateConnection(success=success, connection=connection_instance)


class ChatMutation(graphene.ObjectType):
    create_connection = CreateConnection.Field()
