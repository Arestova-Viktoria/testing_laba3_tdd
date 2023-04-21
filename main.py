from math import sqrt
from scipy import integrate


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
        n = len(matrix1)
        result_matrix = [[0 for i in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
        return result_matrix

    def transp_matrix(self,matrix):
        n = len(matrix)
        m = len(matrix[0])
        t_matrix = [[matrix[j][i] for j in range(n)]for i in range(m)]
        return t_matrix

    def integrate_linear_v(self,a,b,x0,x1):
        func = lambda x: a * x + b
        res, err = integrate.quad(func, x0, x1)
        return res





