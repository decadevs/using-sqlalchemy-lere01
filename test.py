import unittest
from Module.InMemoryStorage import InMemoryStorage
from Module.PostgresTableStorage import PostgresTableStorage


class TestClass(unittest.TestCase):

    def setUp(self):
        InMemoryStorage().create(id = 1, Author = "Aka", Title = "Python Introduction")
        PostgresTableStorage().create(id = 2, Author = "Abdulfatai", Title = "Using SQLAlchemy")
        return super().setUp()

    def tearDown(self):
        InMemoryStorage().delete(id=1)
        InMemoryStorage().delete(id=2)
        return super().tearDown()

    def test_InMemoryStorage(self):
        in_memomry = BooksManager(InMemoryStorage())

        self.assertEqual(in_memomry.fetch(id = 1), {id: 1, Author: "Aka", title: "Python Introduction"})
        self.assertDictEqual(in_memomry.fetch(Author = "Aka"), {id: 1, Author: "Aka", title: "Python Introduction"})
        self.assertDictEqual(in_memomry.fetch(Title = "Ruby", Author = "Aka"), {id: 1, Author: "Aka", Title: "Python Introduction"})
        self.assertListEqual(in_memomry.all(), {1: {id: 1, Author: "Aka", Title: "Python Introduction"}, 2: {id: 2, Author: "Abdulfatai", Title: "Using SQLAlchemy"}})


    def test_PostgresTableStorage(self):
        in_table = BooksManager(PostgresTableStorage())

        self.assertEqual(in_table.fetch(id = 2), 2)
        self.assertDictEqual(in_table.fetch(Author = "Abdulfatai"), {id: 2, Author: "Abdulfatai", Title: "Using SQLAlchemy"})
        self.assertDIctEqual(in_table.fetch(Title = "Using SQLAlchemy", Author = "Abdulfatai"), {id: 2, Author: "Abdulfatai", Title: "Using SQLAlchemy"})
        self.assertListEqual(in_table.all(), {1: {id: 1, Author: "Aka", Title: "Python Introduction"}, 2: {id: 2, Author: "Abdulfatai", Title: "Using SQLAlchemy"}})



if __name__ == "__main__":
    unittest.main()