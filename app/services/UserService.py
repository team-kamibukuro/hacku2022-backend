from sanic import Sanic
from sanic import response
from models.User import User

from repository.UserRepository import *
from setting import async_session

class UserService:

    async def userSiginup(request):

        user = User.User()
        user.usersEmail = request.json['userEmail']
        user.usersName = request.json['userName']
        user.usersPassword = request.json['userPassword']

        await UserRepository.save(user)

        # async with async_session() as session:
        #     session.add(user)
        #     await session.commit()

        return response.json("{\"name\":\"ok\"}")
