import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
from channels.db import database_sync_to_async
from apps.chats.models import *

User = get_user_model()


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        connection = self.room_name
        sender = text_data_json["sender"]
        receiver = text_data_json["receiver"]

        await self.save_message(json.loads(text_data), connection)

        await self.channel_layer.group_send(
            self.room_group_name, {
                "type": "chat_message",
                "message": message,
                "connection": connection,
                "sender": sender,
                "receiver": receiver
            }
        )

    async def chat_message(self, event):
        message = event["message"]
        connection = self.room_name
        sender = event["sender"]
        receiver = event["receiver"]

        await self.send(text_data=json.dumps({
            "message": message,
            "connection": connection,
            "sender": sender,
            "receiver": receiver
        }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    @database_sync_to_async
    def save_message(self, message, connection):
        message_instance = Conversation.objects.create(
            connection=Connection.objects.get(id=connection),
            message=message["message"],
            sender=User.objects.get(id=message["sender"]),
            receiver=User.objects.get(id=message["receiver"])
        )
        return message_instance
