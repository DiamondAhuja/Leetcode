from typing import List

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        combined = [(x, y) for x, y in zip(difficulty, profit)]
        combined.sort(key=lambda x: x[0])
        ans = i = highest = 0
    
        for w in sorted(worker):
            while i < len(combined) and w >= combined[i][0]:
                highest = max(highest, combined[i][1])
                i += 1
            ans += highest
        
        return ans