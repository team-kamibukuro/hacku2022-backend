from sanic import Sanic
from sanic import response
from models.User import User

from repository.UserRepository import *
from setting import async_session


class UserService:

    async def userSiginup(self):
        user = User.User(
            usersName=self.json['userName'],
            usersEmail=self.json['userEmail'],
            usersPassword=self.json['userPassword'])

        await UserRepository.save(user)

        # async with async_session() as session:
        #     session.add(user)
        #     await session.commit()

        return response.json({"name": "ok"})
