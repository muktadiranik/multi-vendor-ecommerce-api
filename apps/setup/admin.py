from django.contrib import admin
from .models import *


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'symbol')


class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'event_type', 'start_date', 'end_date')




admin.site.register(Event, EventAdmin)
admin.site.register(EventType, EventTypeAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(NominationType)
admin.site.register(Nomination)
admin.site.register(AddressType)
admin.site.register(ProductType)
admin.site.register(ProductRateType)
admin.site.register(ContactType)
admin.site.register(Contact)

