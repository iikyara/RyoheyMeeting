"""
ASGI config for RyoheyMeeting project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.conf.urls import url
from django.core.asgi import get_asgi_application

# Fetch Django ASGI application early to ensure AppRegistry is populated
# before importing consumers and AuthMiddlewareStack that may import ORM
# models.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "RyoheyMeeting.settings")
django_asgi_app = get_asgi_application()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import ReactionSocket.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RyoheyMeeting.settings')

application = ProtocolTypeRouter({
    #"https" : django_asgi_app,
    "http" : django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            ReactionSocket.routing.websocket_urlpatterns
        )
    ),
})
