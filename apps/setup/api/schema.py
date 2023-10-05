import graphene
from graphene_django import DjangoObjectType
from apps.setup.models import *


class LanguageObjectType(DjangoObjectType):
    class Meta:
        model = Language
        fields = ('id', 'name', 'code')


class CurrencyObjectType(DjangoObjectType):
    code = graphene.String()
    symbol = graphene.String()

    def resolve_code(self, info):
        return self.code

    def resolve_symbol(self, info):
        return self.symbol

    class Meta:
        model = Currency
        fields = ('id', 'name', 'code', 'symbol')


class NominationTypeObjectType(DjangoObjectType):
    class Meta:
        model = NominationType
        fields = ('id', 'name')


class NominationObjectType(DjangoObjectType):
    class Meta:
        model = Nomination
        fields = '__all__'


class AddressTypeObjectType(DjangoObjectType):
    class Meta:
        model = AddressType
        fields = ('id', 'name')


class ProductTypeObjectType(DjangoObjectType):
    class Meta:
        model = ProductType
        fields = ('id', 'name',)


class ProductRateTypeObjectType(DjangoObjectType):
    class Meta:
        model = ProductRateType
        fields = ('id', 'name',)


class ContactTypeObjectType(DjangoObjectType):
    class Meta:
        model = ContactType
        fields = ('id', 'name',)


class ContactObjectType(DjangoObjectType):

    class Meta:
        model = Contact
        fields = '__all__'


class EventTypeObjectType(DjangoObjectType):
    class Meta:
        model = EventType
        fields = '__all__'
