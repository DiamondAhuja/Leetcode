from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        first = 0
        last = sum(nums)
        for i in range(n-1):
            first += nums[i]
            last -= nums[i]
            if first >= last:
                res += 1
        return res
