from typing import List


class MatrixSum:
    def matrix_sum(self, ma: List[List[int]]) -> None:
        m, n = len(ma), len(ma[0])
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                left = 0 if j == 0 else ma[i][j-1]
                up = 0 if i == 0 else ma[i-1][j]
                corner = 0 if i == 0 or j == 0 else ma[i-1][j-1]


if __name__ == '__main__':
    ms = MatrixSum()

