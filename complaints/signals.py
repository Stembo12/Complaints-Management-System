from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@receiver(post_save, sender=Complaint)
def notify_new_complaint(sender, instance, created, **kwargs):
    if created:  # Only send notification for newly created complaints
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "complaints",  # Group name
            {
                'type': 'complaint_notification',
                'message': f"New complaint logged by {instance.customer}: {instance.details}"
            }
        )
