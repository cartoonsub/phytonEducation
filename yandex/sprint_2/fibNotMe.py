class MatrixFibonacci:
    Q = [[1, 1],
         [1, 0]]

    def __init__(self):
        self.__memo = {}

    def __multiply_matrices(self, M1, M2):
        """Умножение матриц
        (ожидаются матрицы в виде списка список размером 2x2)."""

        a11 = M1[0][0]*M2[0][0] + M1[0][1]*M2[1][0]
        a12 = M1[0][0]*M2[0][1] + M1[0][1]*M2[1][1]
        a21 = M1[1][0]*M2[0][0] + M1[1][1]*M2[1][0]
        a22 = M1[1][0]*M2[0][1] + M1[1][1]*M2[1][1]
        r = [[a11, a12], [a21, a22]]
        return r

    def __get_matrix_power(self, M, p):
        """Возведение матрицы в степень (ожидается p равная степени двойки)."""

        if p == 1:
            return M
        if p in self.__memo:
            return self.__memo[p]
        K = self.__get_matrix_power(M, int(p/2))
        R = self.__multiply_matrices(K, K)
        self.__memo[p] = R
        return R

    def get_number(self, n):
        """Получение n-го числа Фибоначчи
        (в качестве n ожидается неотрицательное целое число)."""
        if n == 0:
            return 0
        if n == 1:
            return 1
        # Разложение переданной степени на степени, равные степени двойки,
        # т.е. 62 = 2^5 + 2^4 + 2^3 + 2^2 + 2^0 = 32 + 16 + 8 + 4 + 1.
        powers = [int(pow(2, b))
                  for (b, d) in enumerate(reversed(bin(n-1)[2:])) if d == '1']
        print(powers)
        # Тоже самое, но менее pythonic: http://pastebin.com/h8cKDkHX

        matrices = [self.__get_matrix_power(MatrixFibonacci.Q, p)
                    for p in powers]
        print(matrices)
        while len(matrices) > 1:
            M1 = matrices.pop()
            M2 = matrices.pop()
            R = self.__multiply_matrices(M1, M2)
            matrices.append(R)
        return matrices[0][0][0]

mfib = MatrixFibonacci()
# number, commits = map(int, '506278  6'.split())
number, commits = map(int, '10  6'.split())
# number, commits = map(int, input().split())

num = mfib.get_number(number + 1)

result = num  % (10 ** commits)
print(result)