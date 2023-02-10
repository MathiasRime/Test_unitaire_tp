import sys

sys.path.append("..")
from src.librairy import Library, Client
from src.book import Book
import unittest


class TestClient(unittest.TestCase):

    def test_check_out_book(self):
        library = Library()
        book = Book("test", "moi")
        library.add_book(book)
        client = Client("oui")
        self.assertEqual(len(client.checked_out_books), 0)
        client.check_out_book(library, "test")
        self.assertEqual(len(client.checked_out_books), 1)
        self.assertTrue(book.is_checked_out)

    def test_check_in_book(self):
        library = Library()
        book = Book("test", "moi")
        library.add_book(book)
        client = Client("oui")
        self.assertEqual(len(client.checked_out_books), 0)
        client.check_out_book(library, "test")
        self.assertEqual(len(client.checked_out_books), 1)
        client.check_in_book(library, "test")
        self.assertEqual(len(client.checked_out_books), 0)
        self.assertFalse(book.is_checked_out)



if __name__ == '__main__':
    unittest.main()