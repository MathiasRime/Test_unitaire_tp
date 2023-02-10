import sys

sys.path.append("..")
from src.librairy import Library
from src.book import Book
import unittest


class TestLibrary(unittest.TestCase):

    def test_add_book(self):
        library = Library()
        book = Book("test", "moi")
        self.assertEqual(len(library.books), 0)
        library.add_book(book)
        self.assertEqual(len(library.books), 1)

    def test_check_out_book(self):
        library = Library()
        book = Book("test", "moi")
        library.add_book(book)
        library.check_out_book("test")
        self.assertTrue(book.is_checked_out)

    def test_check_in_book(self):
        library = Library()
        book = Book("test", "moi")
        library.add_book(book)
        book.check_out()
        library.check_in_book("test")
        self.assertFalse(book.is_checked_out)


if __name__ == '__main__':
    unittest.main()
