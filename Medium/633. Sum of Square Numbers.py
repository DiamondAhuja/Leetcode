class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # both nums < sqrt(c)
        # pointers?
        left = 0
        right = int(c**0.5)
        
        while left <= right:
            total = left ** 2 + right ** 2
            if total == c:
                return True
            elif total < c:
                left += 1
            else:
                right -= 1
        return False
        