import graphene
from apps.core.models import *
from apps.core.api.schema import *


class CoreQuery(graphene.ObjectType):
    about_us = graphene.List(AboutUsObjectType)
    privacy_policy = graphene.List(PrivacyPolicyObjectType)
    terms_and_conditions = graphene.List(TermsAndConditionsObjectType)
    report_types = graphene.List(ReportTypeObjectType)
    bug_reports = graphene.List(BugReportObjectType)
    home_page_content = graphene.List(HomePageObjectType)
    work_flow = graphene.List(GoVeloWorkObjectType)

    def resolve_about_us(self, info, **kwargs):
        return AboutUs.objects.all().order_by('-id')[0:1]

    def resolve_privacy_policy(self, info, **kwargs):
        return PrivacyPolicy.objects.all().order_by('-id')[0:1]

    def resolve_terms_and_conditions(self, info, **kwargs):
        return TermsAndConditions.objects.all().order_by('-id')[0:1]

    def resolve_report_types(self, info, **kwargs):
        return ReportType.objects.all()

    def resolve_bug_reports(self, info, **kwargs):
        return Report.objects.all()

    def resolve_home_page_content(self, info, **kwargs):
        return HomePage.objects.all().order_by('-id')[0:1]

    def resolve_work_flow(self, info, **kwargs):
        return GoVeloWork.objects.all().order_by('-id')[0:3]


core_schema_query = graphene.Schema(query=CoreQuery)
