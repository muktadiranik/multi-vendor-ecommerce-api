from django_filters import FilterSet, NumberFilter, TimeFilter
from django.db.models import Q
from apps.chats.models import *


class ConnectionFilter(FilterSet):
    id = NumberFilter(field_name='id', lookup_expr='exact')
    sender = NumberFilter(method='filter_sender', lookup_expr='exact')
    receiver = NumberFilter(method='filter_receiver', lookup_expr='exact')

    class Meta:
        model = Connection
        fields = "__all__"

    def filter_sender(self, queryset, name, value):
        return Connection.objects.filter(Q(receiver=value) | Q(sender=value))

    def filter_receiver(self, queryset, name, value):
        return Connection.objects.filter(Q(receiver=value) | Q(sender=value))


class ConversationFilter(FilterSet):
    id = NumberFilter(field_name='id', lookup_expr='exact')
    connection_id = NumberFilter(field_name='connection', lookup_expr='exact')
    sender = NumberFilter(field_name='sender', lookup_expr='exact')
    receiver = NumberFilter(field_name='receiver', lookup_expr='exact')
    date_time = TimeFilter(field_name='date_time', lookup_expr='exact')

    class Meta:
        model = Conversation
        fields = "__all__"
