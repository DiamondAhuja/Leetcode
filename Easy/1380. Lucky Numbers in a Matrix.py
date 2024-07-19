from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        rows = {min(x) for x in matrix}
        columns = {max(idx) for idx in zip(*matrix)}
        return list(rows & columns)
