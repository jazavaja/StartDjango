from channels.generic.websocket import AsyncWebsocketConsumer
import json

from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = "general"  # نام اتاق چت
        self.room_group_name = f"chat_{self.room_name}"

        # عضو شدن در گروه
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # ترک گروه
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # دریافت پیام از کلاینت
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # ارسال پیام به گروه
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        # ارسال پیام به کلاینت
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))