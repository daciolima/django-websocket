from django.urls import path

from .consumers import WSConsumer

ws_urlpatterns = [
    path('ws/jokes/', WSConsumer.as_asgi())
]