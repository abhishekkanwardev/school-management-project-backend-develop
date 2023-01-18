from rest_framework.views import APIView
from school_management.utils import Response, ResponseMessage
from rest_framework import status
from .models import Chat, Message
from django.db.models import Q
from .serializers import MessageSerializer, ChatSerializer, ChatUserSerializer





class GetOrCreateChat(APIView):
    
    def get_all_chats_or_create_chat(self, chat_id):
        chats = Chat.objects.filter(id=chat_id).first()
        if chats:
            message = Message.objects.filter(chat=chats)
            message = MessageSerializer(message, many=True)
            return message.data
        else:
            return False
    
    def get(self, request, chat_id):
        chats = self.get_all_chats_or_create_chat(chat_id)
        if chats != False:
            return Response(data=chats, code=status.HTTP_200_OK, message="All Message", status=True)
        else:
            return Response(data={}, code=status.HTTP_404_NOT_FOUND, message="Chat Not Found", status=False)


class CreateNewChat(APIView):
    
    def post(self, request):
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, code=status.HTTP_200_OK, message='', status=True)
        else:
            return Response(data={}, code=status.HTTP_400_BAD_REQUEST, message=serializer.errors, status=False)
        
        
class GetAllChatUsers(APIView):
    
    def get_chat_users(self, chat_id):
        try:
            chat = Chat.objects.get(id=chat_id)
            users = chat.users.all()
            return users
        except Chat.DoesNotExist:
            return False
    
    def get(self, request, chat_id):
        users = self.get_chat_users(chat_id)
        if users:
            serializer = ChatUserSerializer(users, many=True)
            return Response(data=serializer.data, code=status.HTTP_200_OK, message='All Chat Users', status=True)
        else:
            return Response(data={}, code=status.HTTP_400_BAD_REQUEST, message="Chat Not Found", status=False)
    
    
    