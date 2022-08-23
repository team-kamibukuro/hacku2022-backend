from sanic import Sanic
from sanic import response
from models.Room import Room
from .clientJwt import *
from repository.RoomRepository import *
from services.ws.ConnectionManager import *
from services.ws.WsService import managers
import json
from sqlalchemy.ext.serializer import loads, dumps
from setting import async_session


class RoomService:

    async def createRoom(self):

        # for x in dir():
        #     print(x)

        authorization = self.headers.get('Authorization')

        verifyTokenResult = verifyToken(authorization)

        if verifyTokenResult['status'] != 200:
            return response.json(verifyTokenResult, status=400)

        if await RoomRepository.checkRoom(self.json['roomName']):
            return response.json({
                "status": 400,
                "message": "既に存在しているルーム名です。"
            }, status=400)

        room = Room(
            roomName=self.json['roomName'],
            masterUserId=self.json['masterUserId'],
        )

        managers[room.id] = ConnectionManager()

        await RoomRepository.create(room)

        return response.json(room.asDict(), headers={
            "Access-Control-Expose-Headers": "*, Authorization",
            "Authorization": authorization
        })

    async def getRoom(self):

        # for x in dir():
        #     print(x)

        authorization = self.headers.get('Authorization')

        verifyTokenResult = verifyToken(authorization)

        if verifyTokenResult['status'] != 200:
            return response.json(verifyTokenResult, status=400)

        roomModel = await RoomRepository.selectRoomName(self.json['roomName'])

        try:
            res = roomModel.scalars().first().asCreateDict()

            if int(len(managers[res['roomId']].active_connections)) >= 4:
                return response.json({"status": 400, "message": "ルームが満席です。"},
                    headers={
                        "Access-Control-Expose-Headers": "*, Authorization",
                        "Authorization": authorization
                    },
                    status=400
                )
            else:
                return response.json(res, headers={
                    "Authorization": authorization
                })
        except Exception:
            return response.json({"status": 400, "message": "ルーム名が間違っています。"}, status=400)


    async def getMatchingRoom(self):
        authorization = self.headers.get('Authorization')

        verifyTokenResult = verifyToken(authorization)

        if verifyTokenResult['status'] != 200:
            return response.json(verifyTokenResult, status=400)


        for roomId in managers.keys():
            print(len(managers[roomId].active_connections))
            if managers[roomId].isRandomRoom and len(managers[roomId].active_connections) < 4:

                roomModel = await RoomRepository.selectRoomId(roomId)

                res = roomModel.scalars().first().asCreateDict()

                return response.json(res, headers={
                    "Authorization": authorization
                })

        room = Room(
            roomName="Matching-Room-" + str(uuid.uuid4())[-8:],
            masterUserId=self.json['userId'],
            roomIsRandom=True
        )

        managers[room.id] = ConnectionManager()
        managers[room.id].isRandomRoom = True



        await RoomRepository.create(room)

        return response.json(room.asCreateDict(), headers={
            "Access-Control-Expose-Headers": "*, Authorization",
            "Authorization": authorization
        })




