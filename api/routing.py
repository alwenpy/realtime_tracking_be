from django.urls import re_path
from real_time_be.consumer import LocationConsumer

websocket_urlpatterns = [
    re_path(r'ws/location/$', LocationConsumer.as_asgi()),
]
