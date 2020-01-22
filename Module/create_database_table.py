from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import psycopg2

# create connection engine
database_engine = create_engine('postgresql+psycopg2://postgres:password@127.0.0.1:5432/postgres')


# instantiate declarative base class for describing tables by defining classes (declarative)
Base = declarative_base()

# create table class(model)
class Book(Base):
    __tablename__ = 'books'

    record_id = Column(Integer, primary_key = True)
    book_id = Column(String)
    author = Column(String)
    title = Column(String)

# create
Base.metadata.create_all(database_engine)