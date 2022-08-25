from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from setting import async_session, bind
from models.User import *
from sqlalchemy.sql import text


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

    async def selectUserId(userId):
        async with async_session() as session:
            q = select(User).where(User.id == userId)
            result = await (session.execute(q))
            userModel = result.scalars().first().asDict()
            return userModel

    async def updateScore(userId, score):
        async with async_session() as session:

            q_score = text(f"""
                update users 
                set "usersScore" = "usersScore" + ({score} * 1000)
                where "id" = '{userId}'
            """)
            q_badge = text(f"""
                update users 
                    set "rankBadge" = case
                        when "usersScore" <= 5000 then 6
                        when "usersScore" <= 10000 then 5
                        when "usersScore" <= 15000 then 4
                        when "usersScore" <= 20000 then 3
                        when "usersScore" <= 29999 then 2
                        else 1
                    end
                    where "id" = '{userId}'
            """)
            await session.execute(q_score)
            await session.execute(q_badge)

            await session.commit()


    async def selectLogin(userEmail, userPassword):
        async with async_session() as session:
            q = select(User).where(User.usersEmail == userEmail, User.usersPassword == userPassword)

            userModel = await (session.execute(q))


            return userModel
