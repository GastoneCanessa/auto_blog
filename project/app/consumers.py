import json
from channels.generic.websocket import AsyncWebsocketConsumer


class YourConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Quando un client si connette, lo aggiungiamo al gruppo 'posts'
        await self.channel_layer.group_add(
            "posts",
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Quando si disconnette, lo rimuoviamo dal gruppo
        await self.channel_layer.group_discard(
            "posts",
            self.channel_name
        )

    # Questa funzione viene chiamata quando il segnale invia un messaggio al gruppo 'posts'
    async def new_post(self, event):
        await self.send(text_data=json.dumps({
            'title': event["title"],
            'content': event["content"]
        }))