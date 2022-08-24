from sqlalchemy import select

from setting import async_session
from models.Room import *


class RoomRepository():

    # entity = User

    async def create(room: Room):
        async with async_session() as session:
            session.add(room)
            await session.commit()

    async def checkRoom(roomName):
        async with async_session() as session:
            q = select(Room).where(Room.roomName == roomName)
            roomCount = await (session.execute(q))

            return False if int(len(roomCount.all())) == 0 else True

    async def checkRoomId(roomId):
        async with async_session() as session:
            q = select(Room).where(Room.id == roomId)
            roomCount = await (session.execute(q))

            return False if int(len(roomCount.all())) == 0 else True

    async def checkMaterId(roomId):
        async with async_session() as session:
            q = select(Room).where(Room.id == roomId)
            result = await session.execute(q)
            RoomModel = result.scalars().first().asDict()

            return RoomModel["masterUserId"]

    async def selectRoomName(roomName):
        async with async_session() as session:
            q = select(Room).where(Room.roomName == roomName, Room.roomIsRandom == False)

            roomModel = await (session.execute(q))

            return roomModel

    async def selectRoomId(roomId):
        async with async_session() as session:
            q = select(Room).where(Room.id == roomId)

            roomModel = await (session.execute(q))

            return roomModel
