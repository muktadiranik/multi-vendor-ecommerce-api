from django.urls import path
from apps.chats import views


app_name = "chats"
urlpatterns = [
    path("", views.ChatView.as_view(), name="home"),
    path("<str:room_name>/", views.ChatRoom.as_view(), name="room"),
]
