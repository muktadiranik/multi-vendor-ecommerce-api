from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Connection(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="connection_sender", blank=True, null=True)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name="connection_receiver", blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name="connection_created_by", blank=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name="connection_updated_by", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sender.username} in {self.receiver.username}"


class Conversation(models.Model):
    connection = models.ForeignKey(Connection, on_delete=models.CASCADE, blank=True, null=True)
    date_time = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=True, null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="conversation_sender", blank=True, null=True)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name="conversation_receiver", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sender.username} in {self.receiver.username}"
