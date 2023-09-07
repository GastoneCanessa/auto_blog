import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import app.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

# Ottieni l'application ASGI standard di Django per le richieste HTTP
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,  # Usa l'application ASGI standard di Django per le richieste HTTP
    "websocket": URLRouter(
        app.routing.websocket_urlpatterns  # Aggiungi la gestione di WebSocket
    ),
})