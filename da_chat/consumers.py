import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        """在打开WebSocket连接时调用"""
        self.room_name = self.scope["url_route"]["kwargs"]["room"]  # 获取路径中的参数
        # 将用户添加到群组
        async_to_sync(self.channel_layer.group_add)(self.room_name, self.channel_name)
        print(f"{self.channel_name} 进入了聊天室---- {self.room_name}")

        self.accept()

    def disconnect(self, code):
        """当关闭websocket连接时调用"""
        async_to_sync(self.channel_layer.group_discard)(self.room_name, self.channel_name)
        print(f"{self.channel_name} 离开了聊天室---- {self.room_name}")

    def receive(self, text_data):
        """收到消息时调用"""
        json_data = json.loads(text_data)
        async_to_sync(self.channel_layer.group_send)(
            self.room_name,
            {
                "type": "chat_message",  # 调用的函数
                "message": json_data["message"],
                "userName": json_data["userName"],
            },
        )

    def chat_message(self, event):
        """发送消息"""
        self.send(
            json.dumps(
                # 发送到前端的数据格式
                {
                    "sender": event["userName"],
                    "msg": event["message"],
                }
            )
        )
