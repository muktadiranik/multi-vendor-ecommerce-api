import graphene
from django.views.decorators.csrf import csrf_exempt
from apps.setup.models import *
from apps.setup.api.inputs import *
from apps.setup.api.schema import *
from django.contrib.auth import get_user_model

User = get_user_model()


class CreateNominationType(graphene.Mutation):
    class Arguments:
        input = CreateNominationTypeInput()

    success = graphene.Boolean()
    nomination_type = graphene.Field(NominationTypeObjectType)

    @staticmethod
    def mutate(root, info, input=None):
        success = True
        nomination_type_instance = NominationType(name=input.name)
        nomination_type_instance.save()
        return CreateNominationType(success=success, nomination_type=nomination_type_instance)


class UpdateNominationType(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = UpdateNominationTypeInput()

    success = graphene.Boolean()
    nomination_type = graphene.Field(NominationTypeObjectType)

    @staticmethod
    def mutate(root, info, id, input=None):
        success = False
        nomination_type_instance = NominationType.objects.get(pk=id)
        if nomination_type_instance:
            success = True
            nomination_type_instance.name = input.name
            nomination_type_instance.save()
            return UpdateNominationType(success=success, nomination_type=nomination_type_instance)
        return UpdateNominationType(success=success, nomination_type=None)


class DeleteNominationType(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id):
        success = False
        nomination_type_instance = NominationType.objects.get(pk=id)
        if nomination_type_instance:
            success = True
            nomination_type_instance.delete()
            return DeleteNominationType(success=success)
        return DeleteNominationType(success=success)


class CreateNomination(graphene.Mutation):
    class Arguments:
        input = CreateNominationInput()

    success = graphene.Boolean()
    nomination = graphene.Field(NominationObjectType)

    @staticmethod
    def mutate(root, info, input=None):
        success = True
        nomination_instance = Nomination(
            name=input.name,
            nomination_type=NominationType.objects.get(pk=input.nomination_type),
            reason=input.reason,
            email=input.email,
            rental_number=input.rental_number
        )
        nomination_instance.save()
        return CreateNomination(success=success, nomination=nomination_instance)


class UpdateNomination(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = UpdateNominationInput()

    success = graphene.Boolean()
    nomination = graphene.Field(NominationObjectType)

    @staticmethod
    def mutate(root, info, id, input=None):
        success = False
        nomination_instance = Nomination.objects.get(pk=id)
        if nomination_instance:
            success = True
            nomination_instance.name = input.name
            if input.nomination_type:
                nomination_instance.nomination_type = NominationType.objects.get(pk=input.nomination_type)
            nomination_instance.reason = input.reason,
            nomination_instance.email = input.email,
            nomination_instance.rental_number = input.rental_number
            nomination_instance.save()
            return UpdateNomination(success=success, nomination=nomination_instance)
        return UpdateNomination(success=success, nomination=None)


class DeleteNomination(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id):
        success = False
        nomination_instance = Nomination.objects.get(pk=id)
        if nomination_instance:
            success = True
            nomination_instance.delete()
            return DeleteNomination(success=success)
        return DeleteNomination(success=success)


class CreateAddressType(graphene.Mutation):
    class Arguments:
        input = CreateAddressTypeInput()

    success = graphene.Boolean()
    address_type = graphene.Field(AddressTypeObjectType)

    @staticmethod
    def mutate(root, info, input=None):
        success = True
        address_type_instance = AddressType(name=input.name)
        address_type_instance.save()
        return CreateAddressType(success=success, address_type=address_type_instance)


class UpdateAddressType(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = UpdateAddressTypeInput()

    success = graphene.Boolean()
    address_type = graphene.Field(AddressTypeObjectType)

    @staticmethod
    def mutate(root, info, id, input=None):
        success = False
        address_type_instance = AddressType.objects.get(pk=id)
        if address_type_instance:
            success = True
            address_type_instance.name = input.name
            address_type_instance.save()
            return UpdateAddressType(success=success, address_type=address_type_instance)
        return UpdateAddressType(success=success, address_type=None)


class DeleteAddressType(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id):
        success = False
        address_type_instance = AddressType.objects.get(pk=id)
        if address_type_instance:
            success = True
            address_type_instance.delete()
            return DeleteAddressType(success=success)
        return DeleteAddressType(success=success)


class CreateProductType(graphene.Mutation):
    class Arguments:
        input = CreateProductTypeInput()

    success = graphene.Boolean()
    product_type = graphene.Field(ProductTypeObjectType)

    @staticmethod
    def mutate(root, info, input=None):
        success = True
        product_type_instance = ProductType(name=input.name)
        product_type_instance.save()
        return CreateProductType(success=success, product_type=product_type_instance)


class UpdateProductType(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = UpdateProductTypeInput()

    success = graphene.Boolean()
    product_type = graphene.Field(ProductTypeObjectType)

    @staticmethod
    def mutate(root, info, id, input=None):
        success = False
        product_type_instance = ProductType.objects.get(pk=id)
        if product_type_instance:
            product_type_instance.name = input.name
            product_type_instance.save()
            success = True
            return UpdateProductType(success=success, product_type=product_type_instance)
        return UpdateProductType(success=success, product_type=None)


class DeleteProductType(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id):
        success = False
        product_type_instance = ProductType.objects.get(pk=id)
        if product_type_instance:
            product_type_instance.delete()
            success = True
            return DeleteProductType(success=success)
        return DeleteProductType(success=success)


class CreateProductRateType(graphene.Mutation):
    class Arguments:
        input = CreateProductRateTypeInput()

    success = graphene.Boolean()
    product_rate_type = graphene.Field(ProductRateTypeObjectType())

    @staticmethod
    def mutate(root, info, input=None):
        success = True
        product_rate_type_instance = ProductRateType(name=input.name)
        product_rate_type_instance.save()
        return CreateProductRateType(success=success, product_rate_type=product_rate_type_instance)


class UpdateProductRateType(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = UpdateProductRateTypeInput()

    success = graphene.Boolean()
    product_rate_type = graphene.Field(ProductRateTypeObjectType())

    @staticmethod
    def mutate(root, info, id, input=None):
        success = False
        product_rate_type_instance = ProductRateType.objects.get(pk=id)
        if product_rate_type_instance:
            success = True
            product_rate_type_instance.name = input.name
            product_rate_type_instance.save()
            return UpdateProductRateType(success=success, product_rate_type=product_rate_type_instance)
        return UpdateProductRateType(success=success, product_rate_type=None)


class DeleteProductRateType(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id):
        success = False
        product_rate_type_instance = ProductRateType.objects.get(pk=id)
        if product_rate_type_instance:
            success = True
            product_rate_type_instance.delete()
            return DeleteProductRateType(success=success)
        return DeleteProductRateType(success=success)


class CreateContactType(graphene.Mutation):
    class Arguments:
        input = CreateContactTypeInput()

    success = graphene.Boolean()
    contact_type = graphene.Field(ContactTypeObjectType)

    @staticmethod
    def mutate(root, info, input=None):
        success = True
        contact_type_instance = ContactType(name=input.name)
        contact_type_instance.save()
        return CreateContactType(success=success, contact_type=contact_type_instance)


class UpdateContactType(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = UpdateContactTypeInput()

    success = graphene.Boolean()
    contact_type = graphene.Field(ContactTypeObjectType)

    @staticmethod
    def mutate(root, info, id, input=None):
        success = False
        contact_type_instance = ContactType.objects.get(pk=id)
        if contact_type_instance:
            success = True
            contact_type_instance.name = input.name
            contact_type_instance.save()
            return UpdateContactType(success=success, contact_type=contact_type_instance)
        return UpdateContactType(success=success, contact_type=None)


class DeleteContactType(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id):
        success = False
        contact_type_instance = ContactType.objects.get(pk=id)
        if contact_type_instance:
            success = True
            contact_type_instance.delete()
            return DeleteContactType(success=success)
        return DeleteContactType(success=success)


class CreateContact(graphene.Mutation):
    class Arguments:
        input = CreateContactInput()

    success = graphene.Boolean()
    contact = graphene.Field(ContactObjectType)

    @staticmethod
    def mutate(root, info, input=None):
        success = True
        contact_instance = Contact(
            name=input.name,
            email=input.email,
            rental_booking=input.rental_booking,
            contact_type=ContactType.objects.get(pk=input.contact_type),
            description=input.description,
        )
        contact_instance.save()
        return CreateContact(success=success, contact=contact_instance)


class UpdateContact(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = UpdateContactInput()

    success = graphene.Boolean()
    contact = graphene.Field(ContactObjectType)

    @staticmethod
    def mutate(root, info, id, input=None):
        success = False
        contact_instance = Contact.objects.get(pk=id)
        if contact_instance:
            success = True
            contact_instance.name = input.name
            contact_instance.email = input.email
            contact_instance.rental_booking = input.rental_booking
            contact_instance.contact_type = ContactType.objects.get(pk=input.contact_type)
            contact_instance.description = input.description
            contact_instance.save()
            return UpdateContact(success=success, contact=contact_instance)
        return UpdateContact(success=success, contact=None)


class DeleteContact(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id):
        success = False
        contact_instance = Contact.objects.get(pk=id)
        if contact_instance:
            success = True
            contact_instance.delete()
            return DeleteContact(success=success)
        return DeleteContact(success=success)


class SetupMutation(graphene.ObjectType):
    create_nomination_type = CreateNominationType.Field()
    update_nomination_type = UpdateNominationType.Field()
    delete_nomination_type = DeleteNominationType.Field()
    create_nomination = CreateNomination.Field()
    update_nomination = UpdateNomination.Field()
    delete_nomination = DeleteNomination.Field()
    create_address_type = CreateAddressType.Field()
    update_address_type = UpdateAddressType.Field()
    delete_address_type = DeleteAddressType.Field()
    create_product_type = CreateProductType.Field()
    update_product_type = UpdateProductType.Field()
    delete_product_type = DeleteProductType.Field()
    create_product_rate_type = CreateProductRateType.Field()
    update_product_rate_type = UpdateProductRateType.Field()
    delete_product_rate_type = DeleteProductRateType.Field()
    create_contact_type = CreateContactType.Field()
    update_contact_type = UpdateContactType.Field()
    delete_contact_type = DeleteContactType.Field()
    create_contact = CreateContact.Field()
    update_contact = UpdateContact.Field()
    delete_contact = DeleteContact.Field()
