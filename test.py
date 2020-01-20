import unittest
from Module.InMemoryStorage import InMemoryStorage
from Module.PostgresTableStorage import PostgresTableStorage


class TestClass(unittest.TestCase):

    def setUp(self):
        InMemoryStorage().create(id = 1, author = "Aka", title = "Python Introduction")
        PostgresTableStorage().create(id = 2, author = "Abdulfatai", title = "Using SQLAlchemy")
        return super().setUp()

    def tearDown(self):
        InMemoryStorage().delete(id=1)
        InMemoryStorage().delete(id=2)
        return super().tearDown()

    def test_InMemoryStorage(self):
        in_memomry = BooksManager(InMemoryStorage())

        self.assertEqual(in_memomry.fetch(id = 1), 1)
        self.assertDictEqual(in_memomry.fetch(author = "Aka"), {id: 1, author: "Aka", title: "Python Introduction"})
        self.assertDictEqual(in_memomry.fetch(title = "Ruby", author = "Aka"), {id: 1, author: "Aka", title: "Python Introduction"})
        self.assertListEqual(in_memomry.all(), [{id: 1, author: "Aka", title: "Python Introduction"}, {id: 2, author: "Abdulfatai", title: "Using SQLAlchemy"}])


    def test_PostgresTableStorage(self):
        in_table = BooksManager(PostgresTableStorage())

        self.assertEqual(in_table.fetch(id = 2), 2)
        self.assertDictEqual(in_table.fetch(author = "Abdulfatai"), {id: 2, author: "Abdulfatai", title: "Using SQLAlchemy"})
        self.assertDIctEqual(in_table.fetch(title = "Using SQLAlchemy", author = "Abdulfatai"), {id: 2, author: "Abdulfatai", title: "Using SQLAlchemy"})
        self.assertListEqual(in_table.all(), [{id: 1, author: "Aka", title: "Python Introduction"}, {id: 2, author: "Abdulfatai", title: "Using SQLAlchemy"}])



if __name__ == "__main__":
    unittest.main()