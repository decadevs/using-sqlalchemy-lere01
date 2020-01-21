import sqlite3
from .Interface import Interface
from .create_database_table import Book
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class PostgresTableStorage(Interface):
    def __init__(self, database_name):
        self.db_name = database_name

        # create database connectivity
        url = 'sqlite:///' + self.db_name
        db_connectivity = create_engine(url, echo = True)

        # create seesion object to handle the database
        Session = sessionmaker(bind = db_connectivity)
        self.session = Session()


    def create(self, book_id = "", author = "", title = ""):
        # create object of the class Book
        new_record = Book(book_id = book_id, author = author, title = title)
        session = self.session
        
        # add the book to the table
        session.add(new_record)

        # flush the transaction
        session.commit(new_record)

        return 'Record {} sucessfully created'.format(record_id)


    def all(self):
        session = self.session
        # create a Query object
        db_query = session.query(Book)

        # fetch all objects in the table
        db_rows = db_query.all()
        
        # return result object
        return db_rows


    def fetch(self, book_id = None, Author = "", Title = ""):
        db_query = self.session.query(Book)
        
        if book_id != None:
            db_rows = db_query.filter(Book.book_id == book_id)
            return db_rows
            

        elif Author != "":
            db_rows = db_query.filter(Book.author == Author)
            return db_rows


        elif Title != "":
            db_rows = db_query.filter(Book.title == Title)


    def delete(self, book_id = None):
        db_query = self.session.query(Book)
        delete_item = db_query.filter(Book.book_id == book_id)
        pri_key = 0

        for row in delete_item:
            pri_key = row.record_id

        self.session.delete(db_query.get(pri_key))

    


    

