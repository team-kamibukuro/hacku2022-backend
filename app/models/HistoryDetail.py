from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, Boolean
from datetime import datetime
from setting import Base
import uuid
import datetime
from sqlalchemy.ext.declarative import declarative_base
import sys






class HistoryDetail(Base):




    __tablename__ = "history_detail"
    __table_args__ = {'extend_existing': True}

    id = Column('id', String(255), primary_key=True)
    historiesId = Column('historiesId', String(255))
    historyCode = Column('historyCode', String(255))
    createdAt = Column('createdAt', String(255))



    def __init__(self, historiesId='', historyCode=''):
        tz = datetime.timezone(datetime.timedelta(hours=9))


        self.id = str(uuid.uuid4())
        self.historiesId = historiesId
        self.historyCode = historyCode
        self.createdAt = str(datetime.datetime.now(tz))

    def asDict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


    def dict(self):
        return self.__dict__



