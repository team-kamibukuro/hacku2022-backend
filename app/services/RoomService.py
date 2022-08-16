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

