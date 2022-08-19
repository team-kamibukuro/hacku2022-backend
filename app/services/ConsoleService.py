from sanic import Sanic
from sanic import response
from models.User import User
from .clientJwt import *
import json
from sqlalchemy.ext.serializer import loads, dumps

from repository.UserRepository import *
from setting import async_session


class ConsoleService:

    async def getConsoleResult(self):
        authorization = self.headers.get('Authorization')


        return response.json({}, headers={
            "Access-Control-Expose-Headers": "*, Authorization",
            "Authorization": authorization
        })



