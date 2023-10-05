import graphene
from apps.core.api.schema import *
from apps.core.models import *


class CreateReportTypeInput(graphene.InputObjectType):
    name = graphene.String()


class UpdateReportTypeInput(graphene.InputObjectType):
    name = graphene.String()


class CreateReportInput(graphene.InputObjectType):
    name = graphene.String()
    title = graphene.String()
    reason = graphene.String()
    report_type = graphene.ID()


class UpdateReportInput(graphene.InputObjectType):
    name = graphene.String()
    title = graphene.String()
    reason = graphene.String()
    report_type = graphene.ID()
