from sqlalchemy import select
from sqlalchemy.sql import text

from setting import async_session

from models.Question import *


class QuestionRepository:

    # entity = User

    async def choiceQuestion(isDemo):
        async with async_session() as session:
            if isDemo:
                q = text("select * from questions where id like \'DQ_%\' order by random() limit 1")
            else:
                q = text("select * from questions where id like \'Q_%\' order by random() limit 1")
            for r in await session.execute(q):
                return Question(
                    id=r["id"],
                    questionsTitle=r["questionsTitle"],
                    questionsContent=r["questionsContent"]
                )
