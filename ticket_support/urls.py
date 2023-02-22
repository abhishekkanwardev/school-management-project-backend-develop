from django.urls import include, path
from rest_framework import routers
from .views import TicketViewSet

ticket_api_router = routers.SimpleRouter()
ticket_api_router.register("ticket", TicketViewSet, basename="Ticket")

urlpatterns = [
    path("", include(ticket_api_router.urls), name='ticket_api'),
]
