from sanic import Sanic
from sanic import response
from models.User import User
from .clientJwt import *
import json
from sqlalchemy.ext.serializer import loads, dumps

from repository.UserRepository import *
from setting import async_session


class UserService:

    async def userSignup(self):
        user = User(
            usersName=self.json['userName'],
            usersEmail=self.json['userEmail'],
            usersPassword=self.json['userPassword'])

        if await UserRepository.checkEmail(user.usersEmail):
            return response.json({"status": 400, "message": "既に存在しているメールアドレスです。"})

        await UserRepository.save(user)

        return response.json(user.asLoginDict(), headers={
            "Authorization": createToken(user.id, user.usersName)
        })

    async def userLogin(self):
        userEmail = self.json['userEmail']
        userPassword = self.json['userPassword']


        userMpdel = await UserRepository.selectLogin(userEmail, userPassword)

        try:
            res = userMpdel.scalars().first().asLoginDict()
            return response.json(res, headers={
                 "Authorization": createToken(res['userId'], res['userName'])
            })
        except Exception:
            return response.json({"status": 400, "message": "メールアドレスまたはパスワードが間違っています。"})







