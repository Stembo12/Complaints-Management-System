from django.urls import path
from .consumers import ComplaintConsumer

websocket_urlpatterns = [
    path('ws/complaints/', ComplaintConsumer.as_asgi()),
]
