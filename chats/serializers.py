
from rest_framework import serializers
from .models import Chat, Message
from accounts.models import User

class ChatSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Chat
        fields = "__all__"
        
    def validate(self, data):
        """
        Check version already existo or not for this corporate
        """
        
        if data["is_group"] == True:
            if len(data['users']) <= 2:
                raise serializers.ValidationError("Minium 3 user required for group chat")
            if not data.get('name') or data.get('name') == '':
                raise serializers.ValidationError("Name is required for group chat")
        else:
            if len(data['users']) < 2:
                raise serializers.ValidationError("Minium 2 user required for one to one chat")
            elif len(data['users']) > 2:
                raise serializers.ValidationError("Maximum 2 user allowed for one to one chat")
            
            chats = Chat.objects.filter(users__in=data['users']).first()
            if chats:
                raise serializers.ValidationError("One to one chat already exists for this users")
            
        return data
    
    
class MessageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Message
        fields = "__all__"
        
        

class ChatUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']