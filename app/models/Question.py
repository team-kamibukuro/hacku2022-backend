from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, DateTime, TIMESTAMP
from datetime import datetime
from setting import Base
import uuid
import datetime
from sqlalchemy.ext.declarative import declarative_base
import sys






class Question(Base):




    __tablename__ = "questions"
    __table_args__ = {'extend_existing': True}

    id = Column('id', String(255), primary_key=True)
    questionsTitle = Column('questionsTitle', String(255))
    questionsContent = Column('questionsContent', String(4096))

    def __init__(self, id, questionsTitle='', questionsContent=''):

        self.id = id
        self.questionsTitle = questionsTitle
        self.questionsContent = questionsContent

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def dict(self):
        return self.__dict__



