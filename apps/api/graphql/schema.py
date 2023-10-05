from apps.core.api.queries import *
from apps.core.api.mutations import *
from apps.setup.api.queries import *
from apps.setup.api.mutations import *
from apps.shops.api.queries import *
from apps.shops.api.mutations import *
from apps.products.api.queries import *
from apps.products.api.mutations import *
from apps.users.api.queries import *
from apps.users.api.mutations import *
from apps.carts.api.mutations import *
from apps.carts.api.queries import *
from apps.orders.api.queries import *
from apps.orders.api.mutations import *
from apps.chats.api.queries import *
from apps.chats.api.mutations import *


class Query(CoreQuery,
            SetupQuery,
            ShopQuery,
            ProductQuery,
            AuthQuery,
            CartsQuery,
            OrderQuery,
            ChatQuery,
            graphene.ObjectType):
    pass


class Mutation(ShopMutation,
               ProductMutation,
               SetupMutation,
               CoreMutations,
               AuthMutation,
               CartMutation,
               OrderMutation,
               ChatMutation,
               graphene.ObjectType):
    pass
