import graphene
from django.contrib.auth import get_user_model
from .schema import UserObjectType


class AuthQuery(graphene.ObjectType):
    whoami = graphene.Field(UserObjectType)
    users = graphene.List(UserObjectType)

    def resolve_whoami(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Authentication Failure: Your must be signed in')
        return user

    def resolve_users(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Authentication Failure: Your must be signed in')
        if user.profile.role != 'manager':
            raise Exception('Authentication Failure: Must be Manager')
        return get_user_model().objects.all()
