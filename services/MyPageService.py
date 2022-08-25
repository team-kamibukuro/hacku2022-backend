from sanic import Sanic
from sanic import response
from models.Room import Room
from .clientJwt import *
from repository.RoomRepository import *
from services.ws.ConnectionManager import *
from services.ws.WsService import managers
from repository.UserRepository import *
from repository.MyPageRepository import *
import json
from sqlalchemy.ext.serializer import loads, dumps
from setting import async_session


class MyPageService:


    async def getMyPage(self, userId):
        authorization = self.headers.get('Authorization')

        verifyTokenResult = verifyToken(authorization)

        if verifyTokenResult['status'] != 200:
            return response.json(verifyTokenResult, status=400)


        userModel = await UserRepository.selectUserId(userId)


        return response.json({
            "staus": 200,
            "userId": userModel["id"],
            "userName": userModel["usersName"],
            "rankBadge": userModel["rankBadge"],
            "score": userModel["usersScore"]
        }, headers={
            "Access-Control-Expose-Headers": "*, Authorization",
            "Authorization": authorization
        })

    async def getMatchHistory(self, userId):
        authorization = self.headers.get('Authorization')

        verifyTokenResult = verifyToken(authorization)

        if verifyTokenResult['status'] != 200:
            return response.json(verifyTokenResult, status=400)


        matchHistory = await MyPageRepository.getMatchHistory(userId)


        return response.json(matchHistory, headers={
            "Access-Control-Expose-Headers": "*, Authorization",
            "Authorization": authorization
        })

    async def getMatchHistoryDetail(self, userId, roomId):
        authorization = self.headers.get('Authorization')

        verifyTokenResult = verifyToken(authorization)

        if verifyTokenResult['status'] != 200:
            return response.json(verifyTokenResult, status=400)

        matchHistory = await MyPageRepository.getMatchHistoryDetail(userId, roomId)

        return response.json({"test": "ok"}, headers={
            "Access-Control-Expose-Headers": "*, Authorization",
            "Authorization": authorization
        })





