from channels.routing import ProtocolTypeRouter, URLRouter
import app.routing

application = ProtocolTypeRouter({
    'websocket': URLRouter(
        app.routing.websocket_urlpatterns
    ),
})