from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
import graphene
from django.contrib.auth import get_user_model

User = get_user_model()


class CreateUserInput(graphene.InputObjectType):
    username = graphene.String(required=True)
    password = graphene.String(required=True)
    email = graphene.String(required=True)
    name = graphene.String(required=True)


class UpdateUserInput(graphene.InputObjectType):
    password = graphene.String(required=True)
    name = graphene.String(required=True)
