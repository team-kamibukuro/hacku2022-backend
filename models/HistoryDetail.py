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
    historyCode = Column('historyCode', String(4096))
    createdAt = Column('createdAt', String(255))
    isExecuteTest = Column('isExecuteTest', Boolean)
    isProgramError = Column('isProgramError', Boolean)
    programOutput = Column('programOutput', String(1024))
    programError = Column('programError', String(1024))
    testCaseTotal = Column('testCaseTotal', Integer)
    testCaseClearTotal = Column('testCaseClearTotal', Integer)


    def __init__(
            self, historiesId='', historyCode='', isExecuteTest=False, isProgramError=False,
            programOutput='', programError='', testCaseTotal=0, testCaseClearTotal=0):
        tz = datetime.timezone(datetime.timedelta(hours=9))


        self.id = str(uuid.uuid4())
        self.historiesId = historiesId
        self.historyCode = historyCode
        self.isExecuteTest = isExecuteTest
        self.isProgramError = isProgramError
        self.programOutput = programOutput
        self.programError = programError
        self.testCaseTotal = testCaseTotal
        self.testCaseClearTotal = testCaseClearTotal
        self.createdAt = str(datetime.datetime.now(tz))

    def asDict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


    def dict(self):
        return self.__dict__



