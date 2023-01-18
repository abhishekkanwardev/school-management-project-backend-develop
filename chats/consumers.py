import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from chats.models import Chat, Message



def check_user_exist_on_chat(chat_id, user_id):
    user = Chat.objects.filter(id=chat_id, users__in=[user_id]).first()
    if user:
        return True
    else:
        return False


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['chat_id']
        self.room_group_name = 'chat_%s' % self.room_name

        try:
            user = check_user_exist_on_chat(self.room_name, self.scope["user"].id)
        except Exception as e:
            self.accept()
            self.close(code=4004)
        
        if user:
            async_to_sync(self.channel_layer.group_add)(
                self.room_group_name,
                self.channel_name
            )
    
            self.accept()
        else:
            self.accept()
            self.send(text_data=json.dumps({
                'message': "Unauthorized"
            }))
            self.close(code=4004)
            
            
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        
        meg = Message.objects.create(text=message, chat_id=self.room_name, user_id=self.scope["user"].id)
        if meg:
            # Send message to room group
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'sender': self.scope["user"].id,
                }
            )
            

    # Receive message from room group
    def chat_message(self, event):
        self.send(text_data=json.dumps(event))