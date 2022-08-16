from sqlalchemy import select

from setting import async_session
from models.Room import *


class RoomRepository():

    # entity = User



    async def create(room: Room):
        async with async_session() as session:
            session.add(room)
            await session.commit()
