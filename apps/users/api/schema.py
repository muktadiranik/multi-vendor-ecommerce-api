from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model
User = get_user_model()


class UserObjectType(DjangoObjectType):

    def resolve_user_image(self, info):
        if self.user_image:
            self.user_image = info.context.build_absolute_uri(self.user_image.url)
        return self.user_image

    def resolve_user_cover(self, info):
        if self.user_cover:
            self.user_cover = info.context.build_absolute_uri(self.user_cover.url)
        return self.user_cover

    class Meta:
        model = User
        fields = "__all__"
