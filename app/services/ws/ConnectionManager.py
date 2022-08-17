import json




class ConnectionManager:
    def __init__(self):
        self.active_connections= []
        self.full_text = ""

    def __len__(self):
        return len(self.active_connections)

    def set_full_text(self, text: str):
        self.full_text = text

    async def connect(self, request, websocket):
        # await websocket.accept()
        await websocket.send(json.dumps({"event": "CONNECT_SUCCESS"}))

    async def setName(self, request, websocket, roomId, name):
        # await websocket.accept()

        self.active_connections.append({"ws": websocket, "roomId": roomId, "userName": name})
        await websocket.send(json.dumps({"event": "Good_response"}))
        return len(self.active_connections)

    def disconnect(self, websocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket):
        await websocket.send(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection["ws"].send(message)

    async def broadcast_except_me(self, message: str, websocket):
        for connection in self.active_connections:
            if connection["ws"] != websocket:
                await connection["ws"].send(message)

    def get_key(self, request):
        return request.headers['sec-websocket-key']