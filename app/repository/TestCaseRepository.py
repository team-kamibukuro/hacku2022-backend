from sqlalchemy import select

from setting import async_session
from models.Testcase import *


class TestCaseRepository():


    async def checkRoomId(questionId):
        async with async_session() as session:
            q = select(Testcase).where(Testcase.questionsId == questionId)
            testCaseModel = await (session.execute(q))

            return testCaseModel


