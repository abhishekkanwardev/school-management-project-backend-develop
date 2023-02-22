from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from .models import Ticket, TicketConversation, TicketTypes
from accounts.models import User
from .serializers import TicketSerializer, UserListSerializer, TicketListSerializer, ConversationsSerializer

# Create your views here.

class TicketViewSet(ModelViewSet):
    """
    Viewset for Tickets
        list: GET
            type: query_param
                ['assigned'|'raised']
        create: POST
            Raise a new Ticket
        retrieve: GET/pk
            Retreive a ticket
        update: PUT/pk
            Update a ticket
        
        /ticket_types/ : GET
            list all ticket types
        /list_assignees/ : GET
            list all possible assignees
        /post_reply/
            post a reply to a ticket convo
    """
    permission_classes = [IsAuthenticated]
    serializer_class = TicketListSerializer
    queryset = Ticket.objects.all()

    def get_queryset(self):
        if self.request.method == "GET" and not self.detail:
            current_user = self.request.user
            list_type = self.request.query_params.get("type", "raised")
            if list_type == "raised":
                return Ticket.objects.filter(author=current_user)
            elif list_type == "assigned":
                return self.request.user.ticket_assignees.all()
            else:
                raise ValidationError(detail="Invalid query value for type")
        return super().get_queryset()
    
    def get_serializer_class(self):
        if self.request.method == "GET" and self.detail:
            return TicketSerializer
        return super().get_serializer_class()

    def create(self, request: Request, *args, **kwargs):
        data = request.data
        data["author"] = request.user.id
        ticket = self.serializer_class(data=data)
        if ticket.is_valid(raise_exception=True):
            ticket.save(author=request.user)
            TicketConversation.objects.create(
                ticket = ticket.instance,
                user = request.user,
                text = ticket.data["description"]
            )
        return Response(ticket.data, status=status.HTTP_201_CREATED)
    
    @action(methods=["GET"], detail=False)
    def ticket_types(self, request):
        return Response(TicketTypes.choices, status=status.HTTP_200_OK)
    
    @action(methods=["GET"], detail=False)
    def list_assignees(self, request):
        users = User.objects.filter(is_staff=False,is_active=True)
        users = UserListSerializer(users,many=True)
        return Response(users.data, status=status.HTTP_200_OK)
    
    @action(methods=["POST"], detail=False)
    def post_reply(self, request: Request):
        current_user_id = self.request.user.id
        data = self.request.data
        data["user"] = current_user_id
        convo = ConversationsSerializer(data=data)
        if convo.is_valid(raise_exception=True):
            convo.save()
        return Response(data=convo.data,status=status.HTTP_201_CREATED)