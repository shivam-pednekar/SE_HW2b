#from code.calculator import diffOfTwoNos, productOfTwoNos, sumOfTwoNos
import sys
sys.path.insert(1, 'code')
import calculator

import unittest

#Calculator

class TestCalculator(unittest.TestCase):
    def testDivisionOfTwoNos(self):
        """
        Test divisionOfTwoNos works
        """
        a = 2
        b = 4
        result = calculator.divisionOfTwoNos(a,b)
        self.assertEqual(result, 0.5)

    def testSumOfTwoNos(self):
        """
        Test sumOfTwoNos works
        """
        a = 1
        b = 2
        result = calculator.sumOfTwoNos(a,b)
        self.assertEqual(result, 3)

    def testDiffOfTwoNos(self):
        """
        Test diffOfTwoNos works
        """
        a = 1
        b = 2
        result = calculator.diffOfTwoNos(a,b)
        self.assertEqual(result, -1)

    def testProductOfTwoNos(self):
        """
        Test productOfTwoNos works
        """
        a = 1
        b = 2
        result = calculator.productOfTwoNos(a,b)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()