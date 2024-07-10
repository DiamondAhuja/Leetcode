from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        step = 0
        for i, x in enumerate(logs):
            if step != 0 and i != 0 and x == "../":
                step -= 1
                continue
            elif x == "./":
                continue
            elif x != "./" and x != "../":
                step += 1
        return step
