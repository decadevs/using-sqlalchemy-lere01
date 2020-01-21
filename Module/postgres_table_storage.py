from .Interface import Interface
from sqlalchemy import creat_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlite3



Session = sessionmaker(bind = engine)
session = Session
