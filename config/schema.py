import graphene
from apps.api.graphql.schema import *


schema = graphene.Schema(query=Query, mutation=Mutation)
