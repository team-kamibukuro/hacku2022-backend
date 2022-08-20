from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, Boolean
from datetime import datetime
from setting import Base
import uuid
import datetime
from sqlalchemy.ext.declarative import declarative_base
import sys






class History(Base):




    __tablename__ = "questions_histories"
    __table_args__ = {'extend_existing': True}

    id = Column('id', String(255), primary_key=True)
    usersId = Column('usersId', String(255), primary_key=True)
    questionsId = Column('questionsId', String(255), primary_key=True)
    historiesTime = Column('historiesTime', String(255), primary_key=True)
    historiesRanking = Column('historiesRanking', Integer)
    createdAt = Column('createdAt', String(255))



    def __init__(self, usersId='', questionsId='', historiesTime='', historiesRanking=0):
        tz = datetime.timezone(datetime.timedelta(hours=9))

        self.id = str(uuid.uuid4())
        self.usersId = usersId
        self.questionsId = questionsId
        self.historiesTime = historiesTime
        self.historiesRanking = historiesRanking
        self.createdAt = str(datetime.datetime.now(tz))

    def asDict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


    def dict(self):
        return self.__dict__



