import graphene
from apps.setup.api.schema import *
from apps.setup.models import *


class SetupQuery(graphene.ObjectType):
    languages = graphene.List(LanguageObjectType)
    currencies = graphene.List(CurrencyObjectType)
    nomination_types = graphene.List(NominationTypeObjectType)
    nominations = graphene.List(NominationObjectType)
    address_types = graphene.List(AddressTypeObjectType)
    product_types = graphene.List(ProductTypeObjectType)
    product_rate_types = graphene.List(ProductRateTypeObjectType)
    contact_types = graphene.List(ContactTypeObjectType)
    contacts = graphene.List(ContactObjectType)
    event_types = graphene.List(EventTypeObjectType)
 
    def resolve_languages(self, info, **kwargs):
        return Language.objects.all()

    def resolve_currencies(self, info, **kwargs):
        return Currency.objects.all()

    def resolve_nomination_types(self, info, **kwargs):
        return NominationType.objects.all()

    def resolve_nominations(self, info, **kwargs):
        return Nomination.objects.all()

    def resolve_address_types(self, info, **kwargs):
        return AddressType.objects.all()

    def resolve_product_types(self, info, **kwargs):
        return ProductType.objects.all()

    def resolve_product_rate_types(self, info, **kwargs):
        return ProductRateType.objects.all()

    def resolve_contact_types(self, info, **kwargs):
        return ContactType.objects.all()

    def resolve_contacts(self, info, **kwargs):
        return Contact.objects.all()

    def resolve_event_types(self, info, **kwargs):
        return EventType.objects.all()

   

setup_schema_query = graphene.Schema(query=SetupQuery)
