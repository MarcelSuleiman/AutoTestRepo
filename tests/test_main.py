import unittest

from src.main import concat, divide


class TestMain(unittest.TestCase):
    def test_concat(self):
        expectation = "Keyboard Mouse"
        result = concat("Keyboard", "Mouse")

        self.assertEqual(expectation, result)

    def test_divide(self):
        expected = 10.0
        actual = divide(100, 10)
        self.assertEqual(expected, actual)

        expected = 0.1
        actual = divide(10, 100)
        self.assertEqual(expected, actual)

        expected = 2
        actual = divide("10", 5)
        self.assertEqual(expected, actual)

        expected = 2
        actual = divide(10, "5")
        self.assertEqual(expected, actual)

        expected = 2
        actual = divide("10", "5")
        self.assertEqual(expected, actual)

        with self.assertRaises(ZeroDivisionError) as result:
            divide(10, 0)

        expected = "Divide by ZERO is not allowed!"
        self.assertEqual(expected, result.exception.args[0])

