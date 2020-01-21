from .Interface import Interface

class InMemoryStorage(Interface):

    def __init__(self, list_of_books = {}):
        self.books = list_of_books

    def create(self, Author = "", Title = ""):
        record = {}
        record_id = len(self.books) + 1
        record['id'] = record_id
        record['Author'] = Author
        record['Title'] = Title
        self.books[record_id] = record
        return 'Record {} sucessfully created'.format(record_id)

    def all(self):
        return self.books

    def fetch(self, id = None, Author = "", Title = ""):
        if id != None:
            return self.books.get(id)

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


    def delete(self, id = None):
        try:
            del self.books[id]

        except:
            raise Exception('make sure the identity is correct')

            
