from typing import List

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = [[0] * n for _ in range(m)]

        for x, y in indices:
            for i in range(n):
                matrix[x][i] += 1
            for j in range(m):
                matrix[j][y] += 1
        output = 0
        for listt in matrix:
            for num in listt:
                if num % 2 != 0:
                    output += 1

        return output
