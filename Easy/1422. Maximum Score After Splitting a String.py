class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        max_sum = 0
        for i in range(1, n):
            total = s[:i].count('0') + s[i:].count('1')
            max_sum = max(max_sum, total)
        return max_sum