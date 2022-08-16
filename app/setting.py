from sqlalchemy.orm import *
import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

load_dotenv(verbose=True)

dbConnectUrl = "postgresql+asyncpg://{}:{}@{}:5432/{}".format(
        os.environ.get("DB_USER_NAME"),
        os.environ.get("DB_PASSWORD"),
        os.environ.get("DB_HOST"),
        os.environ.get("DB_NAME")
)

print(dbConnectUrl)
bind = create_async_engine(dbConnectUrl, echo=True)




async_session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=bind,
        class_=AsyncSession,
        expire_on_commit=False
    )
)

Base = declarative_base()
Base.query = async_session.query_property()
