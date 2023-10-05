import graphene
import graphql_jwt
from django.contrib.auth import get_user_model
from graphql_jwt.shortcuts import create_refresh_token, get_token
from apps.users.api.schema import *
from .inputs import *

User = get_user_model()


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserObjectType)
    token = graphene.String()
    refresh_token = graphene.String()

    class Arguments:
        input = CreateUserInput(required=True)

    def mutate(self, info, input):
        user = User(
            username=input.username,
            email=input.email,
            name=input.name
        )
        user.set_password(input.password)
        user.save()

        token = get_token(user)
        refresh_token = create_refresh_token(user)

        return CreateUser(user=user, token=token, refresh_token=refresh_token)


class UpdateUser(graphene.Mutation):
    user = graphene.Field(UserObjectType)

    class Arguments:
        input = UpdateUserInput(required=True)

    success = graphene.Boolean()
    user = graphene.Field(UserObjectType)

    def mutate(self, info, input):
        user_instance = User.objects.get(id=info.context.user.id)
        if user_instance:
            if input.password:
                user_instance.set_password(input.password)
            if input.name:
                user_instance.name = input.name
            user_instance.save()
            success = True
            token = get_token(user_instance)
            refresh_token = create_refresh_token(user_instance)

            return UpdateUser(user=user_instance, success=success, token=token, refresh_token=refresh_token)
        return UpdateUser(success=False, user=None)


class AuthMutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()


users_schema = graphene.Schema(mutation=AuthMutation)
