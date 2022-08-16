from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from setting import async_session, bind
from models.User import *


class UserRepository():

    # entity = User

    async def save(user: User):
        async with async_session() as session:
            session.add(user)
            await session.commit()

    async def checkEmail(userEmail):
        async with async_session() as session:
            q = select(User).where(User.usersEmail == userEmail)
            mailCount = await (session.execute(q))

            return False if int(len(mailCount.all())) == 0 else True


    async def selectLogin(userEmail, userPassword):
        async with async_session() as session:
            q = select(User).where(User.usersEmail == userEmail, User.usersPassword == userPassword)

            userModel = await (session.execute(q))


            return userModel
