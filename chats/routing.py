from django.urls import path, re_path

from .consumers import ChatConsumer


websocket_urlpatterns = [
    path('ws/chat/<int:chat_id>/', ChatConsumer.as_asgi()),
    # path('ws/create-chat/', CreateChatConsumer.as_asgi()),
]
