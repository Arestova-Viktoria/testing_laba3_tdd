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

    def test_linear_equation_a_0(self):
        with self.assertRaises(ZeroDivisionError) as e:
            mc = Math_Calculator()
            a = 0
            b = 5
            solution = mc.linear_equation(a, b)
        self.assertEqual('Уравнение не имеет корней',e.exception.args[0])


if __name__ == '__main__':
    unittest.main()
