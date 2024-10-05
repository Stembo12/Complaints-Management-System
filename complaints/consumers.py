import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ComplaintConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Join a common group for complaints
        await self.channel_layer.group_add("complaints", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the group on disconnect
        await self.channel_layer.group_discard("complaints", self.channel_name)

    # Receive new complaint notification
    async def complaint_notification(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
