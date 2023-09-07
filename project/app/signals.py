from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from app.models import Post


# Questo segnale viene attivato ogni volta che viene salvato un oggetto Post.
@receiver(post_save, sender=Post)
def notify_new_post(sender, instance, created, **kwargs):
    # Controllo se il post è appena stato creato
    if created:
        # Ottenere il layer di canale. È come un sistema di messaggistica per Channels.
        channel_layer = get_channel_layer()

        # Invia un messaggio al gruppo 'posts'. Questo sarà ricevuto da tutti i client
        # connessi che "ascoltano" su questo gruppo.
        async_to_sync(channel_layer.group_send)(
            "posts",
            {
                'type': 'new_post',
                'title': instance.title,
                'content': instance.content
            }
        )

        print('segnale inviato ')
    print('kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
