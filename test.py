import unittest
from Module.in_memory_storage import InMemoryStorage
# from Module.PostgresTableStorage import PostgresTableStorage


class TestClass(unittest.TestCase):

    def setUp(self):
        self.book_table = InMemoryStorage()
        self.book_table.create(book_id = 1, Author = "Aka", Title = "Python Introduction")
        self.book_table.create(book_id = 2, Author = "Abdulfatai", Title = "Using SQLAlchemy")
        # PostgresTableStorage().create(Author = "Abdulfatai", Title = "Using SQLAlchemy")
        return super().setUp()

    def tearDown(self):
        self.book_table.delete(book_id = 1)
        self.book_table.delete(book_id = 2)
        # PostgresTableStorage().delete(id=2)
        return super().tearDown()

    def test_InMemoryStorage(self):
        in_memomry = self.book_table
        self.assertDictEqual(in_memomry.fetch(book_id = 1), {'id': 1, 'Author': "Aka", 'Title': "Python Introduction"})
        self.assertDictEqual(in_memomry.fetch(Author = "Aka"), {'id': 1, 'Author': "Aka", 'Title': "Python Introduction"})
        self.assertDictEqual(in_memomry.fetch(Title = "Ruby", Author = "Aka"), {'id': 1, 'Author': "Aka", 'Title': "Python Introduction"})
        self.assertDictEqual(in_memomry.all(), {1: {'id': 1, 'Author': "Aka", 'Title': "Python Introduction"}, 2: {'id': 2, 'Author': "Abdulfatai", 'Title': "Using SQLAlchemy"}})


    # def test_PostgresTableStorage(self):
    #     in_table = BooksManager(PostgresTableStorage())

    #     self.assertEqual(in_table.fetch(book_id = 2), 2)
    #     self.assertDictEqual(in_table.fetch(Author = "Abdulfatai"), {id: 2, Author: "Abdulfatai", Title: "Using SQLAlchemy"})
    #     self.assertDIctEqual(in_table.fetch(Title = "Using SQLAlchemy", Author = "Abdulfatai"), {id: 2, Author: "Abdulfatai", Title: "Using SQLAlchemy"})
    #     self.assertListEqual(in_table.all(), {1: {id: 1, Author: "Aka", Title: "Python Introduction"}, 2: {id: 2, Author: "Abdulfatai", Title: "Using SQLAlchemy"}})



if __name__ == "__main__":
    unittest.main()