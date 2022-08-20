from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, Boolean
from datetime import datetime
from setting import Base
import uuid
import datetime
from sqlalchemy.ext.declarative import declarative_base
import sys






class Room(Base):




    __tablename__ = "rooms"
    __table_args__ = {'extend_existing': True}

    id = Column('id', String(255), primary_key=True)
    masterUserId = Column('masterUserId', String(255))
    roomName = Column('roomName', String(255))
    questionsId = Column('questionsId', String(255))
    roomIsRandom = Column('roomIsRandom', Boolean)



    def __init__(self, masterUserId='', roomName='', roomIsRandom=False):

        self.id = str(uuid.uuid4())
        self.masterUserId = masterUserId
        self.roomName = roomName
        self.roomIsRandom = roomIsRandom

    def asDict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def asCreateDict(self):
        return {
              "status": 200,
              "roomId": self.id,
              "roomName": self.roomName,
              "masterUserId": self.masterUserId
            }

    def dict(self):
        return self.__dict__



