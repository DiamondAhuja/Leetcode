from typing import List

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        moves = 0
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                diff = nums[i-1] - nums[i] + 1
                nums[i] += diff
                moves += diff
        return moves
            