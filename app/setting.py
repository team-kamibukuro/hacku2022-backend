from sqlalchemy.orm import *
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, DateTime
from datetime import datetime
import sys

bind = create_engine("postgresql+asyncpg://hacku:hacku2022@hack-u-database:5432/hack-u-2022", echo=True)

session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=bind)
)


session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=bind
    )
)

Base = declarative_base()
Base.query = session.query_property()
