import unittest

from studentGradeCalculator3 import Student,gradeCalculator

testObj = Student("Suraj",333,89)


class TestCalculatorMethods(unittest.TestCase):

    def testGradeCalculator(self):
        self.assertEqual(gradeCalculator(testObj),"B")


if __name__ == '__main__':
    unittest.main()