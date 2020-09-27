import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from rockimage.config import DATABASE_URL

engine = create_engine(DATABASE_URL)
session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
