from django.urls import re_path

from .consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room>\w+)/$", ChatConsumer.as_asgi()),
]
