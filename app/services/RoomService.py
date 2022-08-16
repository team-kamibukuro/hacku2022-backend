from sanic import Sanic
from sanic import response
from models.Room import Room
from .clientJwt import *
from repository.RoomRepository import *
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
            return response.json(verifyTokenResult)

        room = Room(
            roomName=self.json['roomName'],
            masterUserId=self.json['masterUserId'],
        )

        await RoomRepository.create(room)

        return response.json(room.asDict(), headers={
            "Authorization": authorization
        })


    async def getRoom(self):

        # for x in dir():
        #     print(x)

        authorization = self.headers.get('Authorization')

        verifyTokenResult = verifyToken(authorization)

        if verifyTokenResult['status'] != 200:
            return response.json(verifyTokenResult)


        roomModel = await RoomRepository.create(self.json['roomName'])

        try:
            res = roomModel.scalars().first().asCreateDict()
            return response.json(res, headers={
                 "Authorization": authorization
            })
        except Exception:
            return response.json({"status": 400, "message": "ルーム名が間違っています。"})

