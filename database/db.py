import os

from dotenv import load_dotenv

load_dotenv()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(os.getenv("SQLALCHEMY_DATABASE_URI"))

session_local = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()
