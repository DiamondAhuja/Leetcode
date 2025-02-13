from heapq import heapify, heappop, heappushpop


class Solution:
    def minOperations(self, nums, k):

        heapify(nums)
        ans = 0
        num = heappop(nums)

        while num < k:
            nxt = 2*num+heappop(nums)
            num = heappushpop(nums, nxt)
            ans += 1

        return ans
