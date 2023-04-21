class Math_Calculator:

    def linear_equation(self,a,b):
        try:
            x = - b/a
            return x
        except(ZeroDivisionError):
            raise ZeroDivisionError('Уравнение не имеет корней')

    def quadratic_equation(self, a, b, c):
        pass



