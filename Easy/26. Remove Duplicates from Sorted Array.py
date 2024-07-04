class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n =len(nums)
        newAr = set(nums)
        nums[:n] = sorted(newAr)

        return len(nums)
        