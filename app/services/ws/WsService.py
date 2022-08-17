from sanic import Sanic
from sanic import response
from models.Room import Room
from ..clientJwt import *
from repository.QuestionRepository import *
from repository.RoomRepository import *
import json
import binascii
from models.Question import *

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


                if data_json["event"] == "CONNECT_SUCCESS":

                    masterUserId = await RoomRepository.checkMaterId(roomId)
                    isMaster = True if data_json["playerId"] == masterUserId else False


                    connectCount = await manager.setUser(request, ws, data_json["playerId"], data_json["name"], isMaster, data_json["language"])
                    await RoomRepository.checkMaterId(roomId)
                    if connectCount >= 4:
                        questionModel = await QuestionRepository.choiceQuestion(request)


                        await manager.broadcast(json.dumps(
                            {
                                "event": "READY",
                                "question": {
                                    "id": questionModel.id,
                                    "name": questionModel.questionsTitle,
                                    "context": questionModel.questionsContent
                                },
                                "players": await manager.getPlayers()
                            }, ensure_ascii=False))

                elif data_json["event"] == "UPDATE_CODE":
                    manager.set_full_text(data_json["code"])
                    await manager.broadcast_except_me(json.dumps(
                        {"event": "UPDATE_CODE", "playerId": data_json["playerId"], "code": data_json["code"]}), ws)


                elif data_json["event"] == "UPDATE_HEART":
                    await manager.broadcast_except_me(json.dumps(
                        {"event": "UPDATE_HEART", "playerId": data_json["playerId"], "heart": data_json["heart"]}), ws)


                elif data_json["event"] == "FINISHED":
                    manager.set_full_text(data_json["code"])
                    await manager.broadcast_except_me(json.dumps(
                        {"event": "UPDATE_CODE", "playerId": data_json["playerId"], "code": data_json["code"]}), ws)





        except ws.exceptions.ConnectionClosed:
            manager.disconnect(ws)
            await manager.broadcast(json.dumps(
                {"name": binascii.unhexlify(name).decode('utf-8'), "key": manager.get_key(request),
                 "type": "disconnect",
                 "data": ""}))



