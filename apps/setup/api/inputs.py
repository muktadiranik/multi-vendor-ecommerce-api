import graphene
from apps.setup.models import *
from apps.setup.api.schema import *


class CreateNominationTypeInput(graphene.InputObjectType):
    name = graphene.String()


class UpdateNominationTypeInput(graphene.InputObjectType):
    name = graphene.String()


class CreateNominationInput(graphene.InputObjectType):
    name = graphene.String()
    nomination_type = graphene.ID()
    reason = graphene.String()
    email = graphene.String()
    rental_number = graphene.String()


class UpdateNominationInput(graphene.InputObjectType):
    name = graphene.String()
    nomination_type = graphene.ID()
    reason = graphene.String()
    email = graphene.String()
    rental_number = graphene.String()


class CreateAddressTypeInput(graphene.InputObjectType):
    name = graphene.String()


class UpdateAddressTypeInput(graphene.InputObjectType):
    name = graphene.String()


class CreateProductTypeInput(graphene.InputObjectType):
    name = graphene.String()


class UpdateProductTypeInput(graphene.InputObjectType):
    name = graphene.String()


class CreateProductRateTypeInput(graphene.InputObjectType):
    name = graphene.String()


class UpdateProductRateTypeInput(graphene.InputObjectType):
    name = graphene.String()


class CreateContactTypeInput(graphene.InputObjectType):
    name = graphene.String()


class UpdateContactTypeInput(graphene.InputObjectType):
    name = graphene.String()


class CreateContactInput(graphene.InputObjectType):
    name = graphene.String()
    email = graphene.String()
    rental_booking = graphene.String()
    contact_type = graphene.ID()
    description = graphene.String()


class UpdateContactInput(graphene.InputObjectType):
    name = graphene.String()
    email = graphene.String()
    rental_booking = graphene.String()
    contact_type = graphene.ID()
    description = graphene.String()
