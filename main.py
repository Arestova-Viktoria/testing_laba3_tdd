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

    def sum_matrix(self,matrix1,matrix2):
        n = len(matrix1)
        resultMatrix = [[0] * n for i in range(n)]
        for i in range(n):
            for j in range(n):
                resultMatrix[i][j] = matrix1[i][j] + matrix2[i][j]
        return resultMatrix

    def mult_matrix(self,matrix1,matrix2):
        pass





