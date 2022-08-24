from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, Boolean
from datetime import datetime
from setting import Base
import uuid
import datetime
from sqlalchemy.ext.declarative import declarative_base
import sys






class Testcase(Base):




    __tablename__ = "question_testcases"
    __table_args__ = {'extend_existing': True}

    id = Column('id', String(255), primary_key=True)
    questionsId = Column('questionsId', String(255))
    testcasesInput = Column('testcasesInput', String(2048))
    testcasesOutput = Column('testcasesOutput', String(2048))

    def asDict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


    def dict(self):
        return self.__dict__



