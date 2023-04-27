from channels.generic.websocket import AsyncWebsocketConsumer


class WSConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # self.room_group_name = 'joke'
        await self.channel_layer.group_add('jokes', self.channel_name)
        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard('jokes', self.channel_name)


    async def send_jokes(self, event):
        text_message = event['text']
        await self.send(text_message)



     

