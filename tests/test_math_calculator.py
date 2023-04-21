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

    def test_quadratic_equation_positiveD(self):
        mc = Math_Calculator()
        a = 1
        b = -3
        c = -4
        solution = mc.quadratic_equation(a, b, c)
        result = [4, -1]
        self.assertEqual(solution, result)

    def test_quadratic_equation_nullD(self):
        mc = Math_Calculator()
        a = 1
        b = -2
        c = 1
        solution = mc.quadratic_equation(a, b, c)
        result = [1]
        self.assertEqual(solution, result)

    def test_quadratic_equation_negativeD(self):
        mc = Math_Calculator()
        a = 1
        b = -3
        c = -4
        solution = mc.quadratic_equation(a, b, c)
        result = ['Нет корней!']
        self.assertEqual(solution, result)



if __name__ == '__main__':
    unittest.main()
