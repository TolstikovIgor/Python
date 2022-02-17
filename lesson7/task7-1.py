from typing import List

class Matrix:
    def __init__(self, matrix_data: List[List]):
        self.__matrix = matrix_data

        m_rows = len(self.__matrix)
        self.__matrix_size = frozenset([(m_rows, len(row)) for row in self.__matrix])

    def __add__(self, other: "Matrix") -> "Matrix":
        result = []

        for item in zip(self.__matrix, other.__matrix):
            result.append([sum([j, k]) for j, k in zip(*item)])

        return Matrix(result)

    def __str__(self) -> str:
        return '\n'.join(['\t'.join(map(str, row)) for row in self.__matrix])

matrix1 = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
matrix2 = Matrix([[2, 3], [4, 5], [6, 7], [10, 20]])
print(matrix1, '\n')
print(matrix2, '\n')
print(matrix1 + matrix2)
