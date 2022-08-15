from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, DateTime
from datetime import datetime
from setting import Base
import uuid
import datetime
from sqlalchemy.ext.declarative import declarative_base
import sys






class User(Base):




    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}

    id = Column('id', String(255), primary_key=True, default=str(uuid.uuid4()))
    usersName = Column('users_name', String(255))
    usersEmail = Column('users_mail', String(255))
    usersPassword = Column('users_password', String(255))
    createdAt = Column('created_at', DateTime, default=datetime.datetime.now(), nullable=False)

    # def __init__(self, usersName, usersEmail, usersPassword):
    #     self.id = str(uuid.uuid4())
    #     self.usersName = usersName
    #     self.usersEmail = usersEmail
    #     self.usersPassword = usersPassword
    #     self.createdAt = datetime.datetime.now()




