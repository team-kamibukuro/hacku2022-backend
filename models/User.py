from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, DateTime, TIMESTAMP
from datetime import datetime
from setting import Base
import uuid
import datetime
from sqlalchemy.ext.declarative import declarative_base
import sys






class User(Base):




    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}

    id = Column('id', String(255), primary_key=True)
    usersName = Column('usersName', String(255))
    usersEmail = Column('usersEmail', String(255))
    usersPassword = Column('usersPassword', String(255))
    rankBadge = Column('rankBadge', Integer)
    usersScore = Column('usersScore', Integer)
    createdAt = Column('createdAt', String(32))


    def __init__(self, usersName='', usersEmail='', usersPassword=''):
        tDelta = datetime.timedelta(hours=9)
        JST = datetime.timezone(tDelta, 'JST')

        self.id = str(uuid.uuid4())
        self.usersName = usersName
        self.usersEmail = usersEmail
        self.usersPassword = usersPassword
        self.rankBadge = 6
        self.usersScore = 0
        self.createdAt = str(datetime.datetime.now(JST))

    def asDict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def asLoginDict(self):
        return {
                  "status": 200,
                  "userId": self.id,
                  "userName": self.usersName
                }

    def dict(self):
        return self.__dict__



