import psycopg2
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import DateTime, Float

CONNECTION = "postgres://username:password@host:port/dbname"
engine = create_engine(CONNECTION, echo = True)

Base = declarative_base()

#Start creating tables here
class Exchanges(Base):
   __tablename__ = 'exchanges'
   id = Column(Integer, primary_key=True)
   name = Column(String)
   low = Column(Float)
   high = Column(Float)
   timestamp = Column(DateTime)


Base.metadata.create_all(engine)

#To query
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()
result = session.query(Exchanges).all()



