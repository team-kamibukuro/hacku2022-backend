from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from setting import async_session, bind
from models.User import *
from models.History import *
from models.Room import *
from datetime import datetime as dt
from sqlalchemy.sql import text


class MyPageRepository():


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
                    "startTime": historyWithRoom[2].split('.')[0][:-3],
                    "playerCount": playerCount,
                    "players": players
                })


            return {
                "status": 200,
                "rooms": rooms
            }

    async def getMatchHistoryDetail(userId, roomId):
        async with async_session() as session:
            q_room = select(Room.id, Room.roomName, History.createdAt).join(Room, History.roomId == Room.id, isouter=True).where(History.usersId == userId)
            historyWithRooms = await session.execute(q_room)




            return {
                "status": 200,
                "userId": "id-001",
                "userName": "パオパオ",
                "startTime": "2022/08/26 14:56:41",
                "questionId": "Q_03",
                "questionName": "暗号解読",
                "language": "java",
                "questionContext": "問題文-----問題文-----",
            }



