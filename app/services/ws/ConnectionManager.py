import json


class ConnectionManager:
    def __init__(self):
        self.active_connections= []
        self.full_text = ""

    def __len__(self):
        return len(self.active_connections)

    def set_full_text(self, text: str):
        self.full_text = text

    async def connect(self, request, websocket, name):
        # await websocket.accept()

        self.active_connections.append(websocket)
        await self.broadcast(json.dumps(
            {"name": name, "key": self.get_key(request), "type": "connect",
             "data": self.full_text}))

    def disconnect(self, websocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket):
        await websocket.send(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send(message)

    async def broadcast_except_me(self, message: str, websocket):
        for connection in self.active_connections:
            if connection != websocket:
                await connection.send(message)

    def get_key(self, request):
        return request.headers['sec-websocket-key']