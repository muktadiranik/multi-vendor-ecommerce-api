# chat/views.py
from django.shortcuts import render
from django.views.generic import View


class ChatView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "chats/index.html")


class ChatRoom(View):
    def get(self, request, room_name):
        return render(request, "chats/room.html", {"room_name": room_name})
