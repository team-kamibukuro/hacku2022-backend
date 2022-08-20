from sqlalchemy import select

from setting import async_session
from models.History import *
from models.HistoryDetail import *


class HistoryRepository():


    async def getTestCases(questionId):
        async with async_session() as session:
            q = select(History).where(History.questionsId == questionId)
            testCaseModel = await (session.execute(q))

            return testCaseModel.scalars().all()



