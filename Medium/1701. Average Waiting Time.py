from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        s = customers[0][1]
        n = len(customers)
        startTime = customers[0][0] + customers[0][1]
        for x, y in customers[1:]:
            if x >= startTime:
                s += y
                startTime = x + y
            else:
                s += startTime + y - x
                startTime = startTime + y
        return s / n
