import unittest
from main import Math_Calculator

class MathCalculatorTest(unittest.TestCase):

    def test_construction(self):
        assert Math_Calculator()

    def test_linear_equation(self):
        mc = Math_Calculator()
        a = 2
        b = 5
        solution = mc.linear_equation(a,b)
        result = -2.5
        self.assertEqual(solution, result)


if __name__ == '__main__':
    unittest.main()
