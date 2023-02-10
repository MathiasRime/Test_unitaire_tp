import sys

sys.path.append("..")
from src.calculator import Calculator, calculate
import unittest


class TestCalculator(unittest.TestCase):
    def test_is_add_adding(self):
        self.assertEqual(Calculator.add(1, 1), 2)

    def test_is_subtract_subtracting(self):
        self.assertEqual(Calculator.subtract(1, 1), 0)

    def test_is_multiply_multiplying(self):
        self.assertEqual(Calculator.multiply(2, 2), 4)

    def test_is_divide_dividing(self):
        self.assertEqual(Calculator.divide(4, 2), 2)

    def test_is_dividing_by_zero(self):
        self.assertEqual(Calculator.divide(1, 0), 'cannot divide by 0')

    def test_is_power(self):
        self.assertEqual(Calculator.power(2, 2), 4)

    def test_power_of_zero(self):
        self.assertEqual(Calculator.power(0, 2), 0)

    def test_power_of_1(self):
        self.assertEqual(Calculator.power(1, 2), 1)

    def test_power_zero(self):
        self.assertEqual(Calculator.power(5, 0), 1)

    def test_is_squareroot(self):
        self.assertEqual(Calculator.square_root(4), 2)

    def test_is_squarerooting_negative_int(self):
        self.assertEqual(Calculator.square_root(-4), 'cannot do the square root of a negative number')

    def test_is_calculateKeyword_not_good(self):
        self.assertEqual(calculate("test", 1, 1), 2)

    def test_is_calculating_with_strings(self):
        self.assertEqual(calculate('add', '1', 1), 2)


if __name__ == '__main__':
    unittest.main()
