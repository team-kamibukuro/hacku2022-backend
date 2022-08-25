from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from setting import async_session, bind
from models.User import *
from models.History import *
from models.Room import *
from sqlalchemy.sql import text


class MyPageRepository():

    # entity = User

    async def getMatchHistory(userId):
        async with async_session() as session:
            q_room = select(Room.id, Room.roomName, History.createdAt).join(Room, History.roomId == Room.id, isouter=True).where(History.usersId == userId)
            historyWithRooms = await session.execute(q_room)

            rooms = []

            for historyWithRoom in historyWithRooms:
                players = []

                q_player = select(History, User.usersName).join(User, History.usersId == User.id, isouter=True).where(History.roomId == historyWithRoom[0])
                historyWithUsers = await session.execute(q_player)


                playerCount = 0
                for historyWithUser in historyWithUsers:
                    playerCount += 1
                    players.append(historyWithUser[1])

                rooms.append({
                    "roomId": historyWithRoom[0],
                    "roomName": historyWithRoom[1],
                    "startTime": historyWithRoom[2],
                    "playerCount": playerCount,
                    "players": players
                })


            return {
                "status": 200,
                "rooms": rooms
            }


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
