import sqlite3
from Module.Interface import Interface
from Module.create_database_table import Book
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


    def create(self, book_id = "", Author = "", Title = ""):
        # create object of the class Book
        new_record = Book(book_id = book_id, author = Author, title = Title)
        session = self.session
        
        # add the book to the table
        session.add(new_record)

        # flush the transaction
        session.commit()

        return 'Record sucessfully created'


    def all(self):
        session = self.session
        record = {}

        # create a Query object
        db_query = session.query(Book)

        # fetch all objects in the table
        db_rows = db_query.all()
        
        # return result object
        for row in db_rows:
            reco = {}
            record_id = row.record_id
            reco['id'] = row.book_id
            reco['Author'] = row.author
            reco['Title'] = row.title
            record[row.record_id] = reco

        return record



    def fetch(self, book_id = None, Author = "", Title = ""):
        db_query = self.session.query(Book)
        record = {}
        
        if book_id != None:
            db_rows = db_query.filter(Book.book_id == book_id)
            
            for row in db_rows:
                record['id'] = row.book_id
                record['Author'] = row.author
                record['Title'] = row.title
            
            return record
            

        elif Author != "":
            db_rows = db_query.filter(Book.author == Author)
            
            for row in db_rows:
                record = {}

                record['id'] = row.book_id
                record['Author'] = row.author
                record['Title'] = row.title
            
            return record


        elif Title != "":
            db_rows = db_query.filter(Book.title == Title)
            
            for row in db_rows:
                record = {}

                record['id'] = row.book_id
                record['Author'] = row.author
                record['Title'] = row.title
            
            return record


    def delete(self, book_id = None):
        db_query = self.session.query(Book)
        db_query.filter(Book.book_id == book_id).delete()
        self.session.commit()

    



