from sqlalchemy import select

from setting import async_session
from models.History import *
from models.HistoryDetail import *


class HistoryRepository():




    async def saveHistory(history):
        async with async_session() as session:
            session.add(history)
            await session.commit()

    # async def updateHistory(history):
    #     async with async_session() as session:
    #         result = await (session.execute(select(History).filter(History.id == history.id)))
    #         session.




