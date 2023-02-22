from rest_framework import serializers
from rest_framework.request import Request

from .models import Ticket, TicketTypes, TicketConversation
from accounts.models import User


class ConversationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketConversation
        fields = ["id", "ticket", "text", "created_at", "user"]
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate(self, data):
        user = data["user"]
        ticket: Ticket = data["ticket"]
        try:
            assignee_exists = ticket.assignees.filter(id=user.id).exists()
            author_exists = ticket.author == user
            if not (assignee_exists or author_exists):
                raise serializers.ValidationError("Ticket ID is invalid")
        except Exception as e:
            raise serializers.ValidationError(str(e))
        return super().validate(data)

class TicketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]



class TicketSerializer(serializers.ModelSerializer):
    conversations = serializers.SerializerMethodField()
    class Meta:
        model = Ticket
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]

    def get_conversations(self, obj: Ticket):
        conversations = TicketConversation.objects.filter(ticket=obj)
        conversations = ConversationsSerializer(conversations,many=True)
        return conversations.data


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name")
