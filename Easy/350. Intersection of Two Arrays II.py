from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        count = Counter(nums1)
        for x in nums2:
            if count[x] > 0:
                res.append(x)
                count[x] -= 1
        return res
