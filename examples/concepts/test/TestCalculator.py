import unittest

from calculator import addition


class TestCalculatorMethods(unittest.TestCase):

    def testAddition(self):
        self.assertEqual(addition(10,20) ,30)


if __name__ == '__main__':
    unittest.main()