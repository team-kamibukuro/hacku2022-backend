from sqlalchemy.orm import sessionmaker
from setting import async_session, bind
from models import User



class UserRepository():

    entity = User




    async def save(user: User):
        async with async_session() as session:
            session.add(user)
            await session.commit()






