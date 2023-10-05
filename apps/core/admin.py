from django.contrib import admin
from .models import *

from django_celery_beat.models import (
    IntervalSchedule,
    CrontabSchedule,
    SolarSchedule,
    ClockedSchedule,
    PeriodicTask,
)


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'created_at',)


@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(admin.ModelAdmin):
    list_display = ('title',  'created_at', )


@admin.register(TermsAndConditions)
class TermsAndConditionsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', )


class ReportTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ReportAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'reason', 'report_type', 'created_at')


class HomePageAdmin(admin.ModelAdmin):
    list_display = ('site_logo', 'site_video')


class GoVeloWorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'icon')


admin.site.register(ReportType, ReportTypeAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(HomePage, HomePageAdmin)
admin.site.register(GoVeloWork, GoVeloWorkAdmin)

admin.site.unregister(SolarSchedule)
admin.site.unregister(ClockedSchedule)
admin.site.unregister(PeriodicTask)
admin.site.unregister(IntervalSchedule)
admin.site.unregister(CrontabSchedule)
