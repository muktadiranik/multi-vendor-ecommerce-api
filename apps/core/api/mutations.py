import graphene
from apps.core.api.schema import *
from apps.core.api.inputs import *
from apps.core.models import *

class CreateReportType(graphene.Mutation):
    class Arguments:
        input = CreateReportTypeInput(required=True)

    report_type = graphene.Field(ReportTypeObjectType)

    def mutate(self, info, input=None):
        report_type = ReportType.objects.create(
            name=input.name
        )
        return CreateReportType(report_type=report_type)


class UpdateReportType(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = UpdateReportTypeInput(required=True)

    report_type = graphene.Field(ReportTypeObjectType)

    def mutate(self, info, id, input=None):
        report_type = ReportType.objects.get(pk=id)
        report_type.name = input.name
        report_type.save()
        return UpdateReportType(report_type=report_type)


class DeleteReportType(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id):
        report_type = ReportType.objects.get(pk=id)
        report_type.delete()
        return DeleteReportType(success=True)


class CreateReport(graphene.Mutation):
    class Arguments:
        input = CreateReportInput(required=True)

    report = graphene.Field(BugReportObjectType)

    def mutate(self, info, input=None):
        report = Report.objects.create(
            name=input.name,
            title=input.title,
            reason=input.reason,
            report_type=ReportType.objects.get(pk=input.report_type)
        )
        return CreateReport(report=report)


class UpdateReport(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = UpdateReportInput(required=True)

    report = graphene.Field(BugReportObjectType)

    def mutate(self, info, id, input=None):
        report = Report.objects.get(pk=id)
        report.name = input.name
        report.title = input.title
        report.reason = input.reason
        report.report_type = ReportType.objects.get(pk=input.report_type)
        report.save()
        return UpdateReport(report=report)


class DeleteReport(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id):
        report = Report.objects.get(pk=id)
        report.delete()
        return DeleteReport(success=True)


class CoreMutations(graphene.ObjectType):
    create_report_type = CreateReportType.Field()
    update_report_type = UpdateReportType.Field()
    delete_report_type = DeleteReportType.Field()
    create_report = CreateReport.Field()
    update_report = UpdateReport.Field()
    delete_report = DeleteReport.Field()
