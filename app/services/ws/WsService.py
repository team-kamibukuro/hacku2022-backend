from sanic import Sanic
from sanic import response
from models.Room import Room
from ..clientJwt import *
from repository.QuestionRepository import *
from repository.RoomRepository import *
import json
import random
import binascii
from models.Question import *

from sanic import response
from sqlalchemy.ext.serializer import loads, dumps
from setting import async_session

managers = {}
is_public = {}
name = {}

commentLanguage = {
    "c": "// ",
    "charp": "// ",
    "cpp": "// ",
    "go": "// ",
    "java": "// ",
    "javascript": "// ",
    "php": "// ",
    "perl": "# ",
    "python": "# ",
    "r": "# ",
    "ruby": "# ",
    "rust": "// ",
    "scala": "// ",
    "swift": "// ",
    "typescript": "// ",

}


class WsService:






    async def playGame(request,  ws, roomId):
        manager = managers[roomId]
        await manager.connect(request, ws)



        try:
            while True:
                data = await ws.recv()
                data_json = json.loads(data)


                if data_json["event"] == "UPDATE_CODE":
                    await manager.broadcast_except_me(json.dumps(
                        {"event": "UPDATE_CODE", "playerId": data_json["playerId"], "code": data_json["code"]}), ws)


                elif data_json["event"] == "ATTACK":

                    code = """
def is_prime(n):
    if n < 2:
        return False
    for k in range(2, int(n/2)+1):
        if n % k == 0:
            return False
    return True
                            """

                    comment = commentLanguage[data_json["language"]]

                    if data_json["attackType"] == "INDENT_INJECTION":
                        code = data_json["code"]

                    elif data_json["attackType"] == "COMMENTOUT_INJECTION":
                        # code = data_json["code"]
                        index = 0
                        for i in range(10):
                            startChar = random.randint(0, len(code))
                            index = code.find("\n", startChar, len(code))
                            if code[index+2:index+3] != "\n":
                                break

                        if index == -1:
                            code = comment + code
                        else:
                            index = index + 2
                            code = code[:index] + comment + code[index:]


                    elif data_json["attackType"] == "TBC_POISONING":
                        code = data_json["code"]

                    await manager.broadcast_except_me(json.dumps(
                        {
                            "event": "ATTACK",
                            "attackType": data_json["attackType"],
                            "playerId": data_json["playerId"],
                            "language": data_json["language"],
                            "name": data_json["name"],
                            "code": code
                        }, ensure_ascii=False), ws)


                elif data_json["event"] == "CONNECT_SUCCESS":

                    masterUserId = await RoomRepository.checkMaterId(roomId)
                    isMaster = True if data_json["playerId"] == masterUserId else False


                    connectCount = await manager.setUser(request, ws, data_json["playerId"], data_json["name"], isMaster, data_json["language"])
                    await RoomRepository.checkMaterId(roomId)
                    if connectCount >= 2:
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


                elif data_json["event"] == "UPDATE_HEART":
                    await manager.broadcast_except_me(json.dumps(
                        {"event": "UPDATE_HEART", "playerId": data_json["playerId"], "heart": data_json["heart"]}), ws)


                elif data_json["event"] == "FINISHED":
                    await manager.broadcast_except_me(json.dumps(
                        {"event": "FINISHED", "playerId": data_json["playerId"]}), ws)





        except ws.exceptions.ConnectionClosed:
            manager.disconnect(ws)
            await manager.broadcast(json.dumps(
                {"name": binascii.unhexlify(name).decode('utf-8'), "key": manager.get_key(request),
                 "type": "disconnect",
                 "data": ""}))



