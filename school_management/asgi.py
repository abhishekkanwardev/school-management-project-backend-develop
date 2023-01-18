"""
ASGI config for school_management project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school_management.settings')

# application = get_asgi_application()




# import os
# import django
# from channels.routing import get_default_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "school_management.settings")
# django.setup()
# application = get_default_application()

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter

from chats.routing import websocket_urlpatterns

from django.urls import include
from django.urls import path, re_path
from chats.consumers import ChatConsumer

from channels.auth import AuthMiddlewareStack
from .middlewares import TokenAuthMiddleWare
from channels.security.websocket import AllowedHostsOriginValidator

# application = ProtocolTypeRouter({
#     'http': get_asgi_application(),
#     'websocket': TokenAuthMiddleWare(
#         AllowedHostsOriginValidator(
#             URLRouter(
#                 websocket_urlpatterns
#             )
#         )
#     )
# })



application = ProtocolTypeRouter(
    {   "http": get_asgi_application(),
        "websocket": TokenAuthMiddleWare(
            URLRouter(
            websocket_urlpatterns
            )
        )
    }
)


# application = ProtocolTypeRouter({
#     'http': get_asgi_application(),
#     'websocket': URLRouter(
#         [
#             path('ws/chat', ChatConsumer.as_asgi()),
#         ]
#     )
# })