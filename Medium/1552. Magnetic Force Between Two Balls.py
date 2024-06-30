from typing import List

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        def numBalls(f: int) -> int:
            balls = 1
            lastPosition = position[0]
            for pos in position[1:]:
                if pos - lastPosition >= f:
                    balls += 1
                    lastPosition = pos
            return balls
        
        l, r = 1, position[-1] - position[0]
        while l < r:
            mid = (l + r + 1) // 2
            if numBalls(mid) >= m:
                l = mid
            else:
                r = mid - 1
        
        return l