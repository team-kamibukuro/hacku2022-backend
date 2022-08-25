from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from setting import async_session, bind
from models.User import *
from models.History import *
from models.Room import *
from models.Question import *
from models.HistoryDetail import *
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
            q_any= select(User.id, User.usersName, Room.id, Room.roomName, History.createdAt, Question.id, Question.questionsTitle, Question.questionsContent, History.language, History.id).join(Room, History.roomId == Room.id, isouter=True).join(User, History.usersId == User.id).join(Question, History.questionsId == Question.id).where(History.usersId == userId, History.roomId == roomId)
            historyWithAnys = await session.execute(q_any)




            for historyWithAny in historyWithAnys:
                gameResult = []
                histories = []

                q_player = select(User.usersName, History.historiesTime, User.rankBadge, History.historiesRanking).join(User, History.usersId == User.id, isouter=True).where(History.roomId == roomId)
                historyWithUsers = await session.execute(q_player)

                for historyWithUser in historyWithUsers:
                    gameResult.append({
                        "userName": historyWithUser[0],
                        "scoreTime": historyWithUser[1],
                        "rankBadge": historyWithUser[2],
                        "ranking": historyWithUser[3]
                    })

                q_history_detail = select(HistoryDetail).where(HistoryDetail.historiesId == historyWithAny[9])
                historyDetailModels = await session.execute(q_history_detail)


                for historyDetailModel in historyDetailModels:

                    histories.append({
                        "historyId": historyDetailModel[0].id,
                        "debugTime": historyDetailModel[0].createdAt.split('.')[0],
                        "code": historyDetailModel[0].historyCode,
                        "isExecuteTest": historyDetailModel[0].isExecuteTest,
                        "isProgramError": historyDetailModel[0].isProgramError,
                        "programOutput": historyDetailModel[0].programOutput,
                        "programError": historyDetailModel[0].programError,
                        "isClearTestCases": True if historyDetailModel[0].testCaseTotal == historyDetailModel[0].testCaseClearTotal else False,
                        "testCaseTotal": historyDetailModel[0].testCaseTotal,
                        "testCaseClearTotal": historyDetailModel[0].testCaseClearTotal
                    })
                return {
                    "status": 200,
                    "userId": historyWithAny[0],
                    "userName": historyWithAny[1],
                    "roomId": historyWithAny[2],
                    "roomName": historyWithAny[3],
                    "startTime": historyWithAny[4].split('.')[0],
                    "questionId": historyWithAny[5],
                    "questionName": historyWithAny[6],
                    "questionContext": historyWithAny[7],
                    "language": historyWithAny[8],
                    "gameResult": sorted(gameResult, key=lambda x: x['ranking']),
                    "histories": sorted(histories, key=lambda x:x['debugTime'], reverse=True)
                }



