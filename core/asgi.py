import os

from django.core.asgi import get_asgi_application 
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack
import complaints.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_asgi_application()

application = ProtocolTypeRouter({
    'http': application,  
    "websocket": AuthMiddlewareStack(
        URLRouter(
            complaints.routing.websocket_urlpatterns
        )
    ),
}) 


