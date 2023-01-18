
from django.urls import path
from .views import GetOrCreateChat, CreateNewChat, GetAllChatUsers


urlpatterns = [ 
	path('get-or-create-chat/<int:chat_id>', GetOrCreateChat.as_view(), name='chat'),
	path('create-new-chat', CreateNewChat.as_view(), name='create-chat'),
	path('get-chat-users/<int:chat_id>', GetAllChatUsers.as_view(), name='get-chat-users'),
]