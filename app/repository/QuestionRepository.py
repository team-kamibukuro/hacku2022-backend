from sqlalchemy import select
from sqlalchemy.sql import text

from setting import async_session

from models.Question import *


class QuestionRepository:

    # entity = User

    async def choiceQuestion(self):
        async with async_session() as session:
            q = text("select * from questions order by random() limit 1")
            for r in await session.execute(q):
                return Question(
                    id=r["id"],
                    questionsTitle=r["questionsTitle"],
                    questionsContent=r["questionsContent"]
                )
