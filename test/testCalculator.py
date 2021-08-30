#from code.calculator import diffOfTwoNos, productOfTwoNos, sumOfTwoNos
import sys
sys.path.insert(1, '../code')
import calculator

import unittest


class TestCalculator(unittest.TestCase):
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