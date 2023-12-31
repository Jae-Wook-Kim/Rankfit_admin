from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from main import consumers

# application = ProtocolTypeRouter({
#     'websocket': URLRouter([
#         path('ws/notifications/', consumers.NotificationConsumer.as_asgi()),
#     ]),
# })

websocket_urlpatterns = [
    path('ws/notifications/', consumers.NotificationConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket': URLRouter(websocket_urlpatterns),
})