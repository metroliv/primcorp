import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat.routing import websocket_urlpatterns  # This is the correct import

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'primcorp.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns  # This will include the URL patterns defined in `chat/routing.py`
        )
    ),
})
