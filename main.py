from math import sqrt


class Math_Calculator:

    def linear_equation(self,a,b):
        try:
            x = - b/a
            return x
        except(ZeroDivisionError):
            raise ZeroDivisionError('Уравнение не имеет корней')

    def quadratic_equation(self, a, b, c):
        res = []
        discr = b**2 - 4 * a * c
        if discr > 0:
            x1 = (sqrt(discr) - b) / (2 * a)
            x2 = (- sqrt(discr) - b) / (2 * a)
            res.append(x1)
            res.append(x2)
        if discr == 0:
            x = (sqrt(discr) - b) / (2 * a)
            res.append(x)
        if discr < 0:
            res.append('Нет корней!')
        return res







