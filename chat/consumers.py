from django.contrib.auth.models import User
from channels.db import database_sync_to_async
from .models import Message
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'chat_room'
        self.room_group_name = f'chat_{self.room_name}'

        # Join the room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Send a message to notify connection
        await self.send(text_data=json.dumps({
            'message': 'You are connected to the chat.'
        }))

    async def disconnect(self, close_code):
        # Leave the room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        parent_message_id = text_data_json.get('parent_message')  # Get parent message if it's a reply
        user = self.scope['user']  # Get the user who sent the message

        # If it's a reply, find the parent message
        parent_message = None
        if parent_message_id:
            parent_message = await self.get_message(parent_message_id)

        # Save the message to the database
        message_obj = await self.save_message(user, message, parent_message)

        # Send the message to the room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': user.username,  # Send the username of the sender
                'parent_message_id': parent_message_id  # Send the parent message ID if it's a reply
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        parent_message_id = event.get('parent_message_id')

        # Send the message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'parent_message_id': parent_message_id
        }))

    @database_sync_to_async
    def save_message(self, user, message, parent_message):
        # Save the message in the database
        return Message.objects.create(user=user, message=message, parent_message=parent_message)

    @database_sync_to_async
    def get_message(self, message_id):
        # Fetch the message from the database
        return Message.objects.get(id=message_id)
