import sys

sys.path.append("..")
from src.book import Book
import unittest


class TestBook(unittest.TestCase):
    def test_is_a_book_instance(self):
        b = Book('test', 'moi')
        self.assertIsInstance(b, Book)

    def test_is_checkout(self):
        b = Book('test', 'moi')
        Book.check_out(b)
        self.assertTrue(b.is_checked_out)

    def test_is_checkin(self):
        b = Book('test', 'moi')
        Book.check_in(b)
        self.assertFalse(b.is_checked_out)


if __name__ == '__main__':
    unittest.main()
