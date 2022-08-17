from sanic import Sanic
from sanic import response
from models.Room import Room
from ..clientJwt import *
from repository.RoomRepository import *
import json
import binascii

from sanic import response
from sqlalchemy.ext.serializer import loads, dumps
from setting import async_session

managers = {}
is_public = {}
name = {}


class WsService:


    async def playGame(request,  ws, roomId):
        manager = managers[roomId]
        await manager.connect(request, ws)

        try:
            while True:
                data = await ws.recv()
                data_json = json.loads(data)

                if data_json["type"] == "chat":
                    await manager.broadcast(json.dumps(
                        {"name": binascii.unhexlify(name).decode('utf-8'), "key": manager.get_key(request),
                         "type": "chat", "data": data_json["data"]}))

                elif data_json["type"] == "cursormove":
                    await manager.broadcast_except_me(json.dumps(
                        {"name": binascii.unhexlify(name).decode('utf-8'), "key": manager.get_key(request),
                         "type": "cursormove", "data": data_json["data"]}), ws)

                elif data_json["type"] == "selection":
                    await manager.broadcast_except_me(json.dumps(
                        {"name": binascii.unhexlify(name).decode('utf-8'), "key": manager.get_key(request),
                         "type": "selection", "data": data_json["data"]}), ws)

                elif data_json["type"] == "attack":
                    if data_json["attack_type"] == "injection":
                        manager.set_full_text(data_json["data"]["full_text"].replace(' ', ''))
                    # manager.set_full_text(data_json["data"]["full_text"])
                    await manager.broadcast_except_me(json.dumps(
                        {"name": name, "key": manager.get_key(request),
                         "type": "edit", "data": data_json["data"]}), ws)

                elif data_json["type"] == "edit":
                    manager.set_full_text(data_json["data"]["full_text"])
                    await manager.broadcast_except_me(json.dumps(
                        {"name": name, "key": manager.get_key(request),
                         "type": "edit", "data": data_json["data"]}), ws)

        except ws.exceptions.ConnectionClosed:
            manager.disconnect(ws)
            await manager.broadcast(json.dumps(
                {"name": binascii.unhexlify(name).decode('utf-8'), "key": manager.get_key(request),
                 "type": "disconnect",
                 "data": ""}))



