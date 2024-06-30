from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        maxx, sub_max = nums[0], nums[0]
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                sub_max += nums[i]
                maxx = max(sub_max, maxx)
            else:
                sub_max = nums[i]

        return maxx
