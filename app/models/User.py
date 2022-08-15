from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, DateTime
from datetime import datetime
from app.setting import Base
import uuid
import datetime
from sqlalchemy.ext.declarative import declarative_base
import sys






class User(Base):




    __tablename__ = "users"  # テーブル名を指定
    id = Column(Integer, primary_key=True)
    usersName = Column('users_name', String(255))
    usersMail = Column('users_mail', String(255))
    usersPassword = Column('users_password', String(255))
    createdAt = Column('created', DateTime, default=datetime.now, nullable=False)

    def __init__(self, usersName, usersMail, usersPassword):
        self.id = str(uuid.uuid4())
        self.usersName = usersName
        self.usersPassword = usersPassword
        self.createdAt = datetime.datetime.now()




