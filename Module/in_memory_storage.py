from .interface import Interface

class InMemoryStorage(Interface):

    def __init__(self, list_of_books = {}):
        self.books = list_of_books

    def create(self, book_id = "", Author = "", Title = ""):
        record = {}
        record_id = len(self.books) + 1
        record['id'] = book_id
        record['Author'] = Author
        record['Title'] = Title
        self.books[record_id] = record
        return 'Record {} sucessfully created'.format(record_id)

    def all(self):
        return self.books

    def fetch(self, book_id = None, Author = "", Title = ""):
        if book_id != None:
            book = self.books

            for id in book:
                if book[id]['id'] == book_id:
                    return book.get(id)

        elif Author != "":
            book = self.books

            for id in book:
                if book[id]['Author'] == Author:
                    return book.get(id)


        elif Title != "":
            book = self.books

            for id in book:
                if book[id]['Title'] == Title:
                    return book.get(id)


    def delete(self, book_id = None):
        try:
            book = self.books

            for id in book:
                if book[id]['id'] == book_id:
                    del book[id]

        except:
            raise Exception('make sure the identity is correct')

            
