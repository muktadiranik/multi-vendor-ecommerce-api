from graphene_django import DjangoObjectType
from apps.core.models import *
from graphene import String


class AboutUsObjectType(DjangoObjectType):

    content = String()

    def resolve_content(self, info):
        if self.description:
            return self.description.html

    class Meta:
        model = AboutUs
        fields = '__all__'
        include = ['content']

    def resolve_image(self, info):
        if self.image:
            self.image = info.context.build_absolute_uri(self.image.url)
        return self.image


class PrivacyPolicyObjectType(DjangoObjectType):

    content = String()

    def resolve_content(self, info):
        if self.description:
            return self.description.html

    class Meta:
        model = PrivacyPolicy
        fields = '__all__'
        include = ['content']


class TermsAndConditionsObjectType(DjangoObjectType):

    content = String()

    def resolve_content(self, info):
        if self.description:
            return self.description.html

    class Meta:
        model = TermsAndConditions
        fields = '__all__'
        include = ['content']


class ReportTypeObjectType(DjangoObjectType):
    class Meta:
        model = ReportType
        fields = ('id', 'name')


class BugReportObjectType(DjangoObjectType):
    class Meta:
        model = Report
        fields = ('id', 'name', 'title', 'reason', 'report_type', 'created_at')


class HomePageObjectType(DjangoObjectType):
    class Meta:
        model = HomePage
        fields = '__all__'

    def resolve_site_logo(self, info):
        if self.site_logo:
            self.site_logo = info.context.build_absolute_uri(self.site_logo.url)
        return self.site_logo

    def resolve_site_video(self, info):
        if self.site_video:
            self.site_video = info.context.build_absolute_uri(self.site_video.url)
        return self.site_video


class GoVeloWorkObjectType(DjangoObjectType):
    class Meta:
        model = GoVeloWork
        fields = '__all__'

    def resolve_icon(self, info):
        if self.icon:
            self.icon = info.context.build_absolute_uri(self.icon.url)
        return self.icon
