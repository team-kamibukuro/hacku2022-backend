import json
import binascii




class ConnectionManager:
    def __init__(self):
        self.active_connections= []
        self.full_text = ""
        self.isRandomRoom = False
        self.finishedUserCount = 0
        self.finishedUser = []
        self.historyModels = {}

    def __len__(self):
        return len(self.active_connections)

    def set_full_text(self, text: str):
        self.full_text = text

    async def connect(self, request, websocket):
        # await websocket.accept()
        await websocket.send(json.dumps({"event": "CONNECT_SUCCESS"}))

    async def setUser(self, request, websocket, id, name, isMaster, language):
        # await websocket.accept()

        self.active_connections.append({"ws": websocket, "id": id, "name": name, "isMaster": isMaster, "language": language})
        await websocket.send(json.dumps({"event": "Good_response"}))
        return len(self.active_connections)


    async def getPlayers(self):
        result = []



        for tmpActiveConnection in self.active_connections:

            tmp = tmpActiveConnection.copy()

            tmp.pop('ws')
            result.append(tmp)

        return result


    async def disconnect(self, websocket):
        for i, connection in enumerate(self.active_connections):
            if connection["ws"] == websocket:
                self.active_connections.pop(i)
                self.finishedUserCount -= 1
                websocket.close()



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