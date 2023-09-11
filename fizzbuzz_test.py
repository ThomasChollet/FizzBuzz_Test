import unittest
from fizzbuzz import fizzbuzz

class TestFizzbuzz(unittest.TestCase):
    def test_fizz(self):
        result = fizzbuzz(3)
        self.assertEqual(result, "Fizz")

    def test_buzz(self):
        result = fizzbuzz(5)
        self.assertEqual(result, "Buzz")

    def test_fizzbuzz(self):
        result = fizzbuzz(15)
        self.assertEqual(result, "FizzBuzz")

    def test_not_fizz_nor_buzz(self):
        result = fizzbuzz(7)
        self.assertEqual(result, "7")

if __name__ == '__main__':
    unittest.main()