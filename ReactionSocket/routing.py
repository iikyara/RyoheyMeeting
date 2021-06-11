from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/ReactionSocket/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/ReactionSocket/(?P<conf_id>\w+)/$', consumers.ReactionConsumer.as_asgi()),
]
