class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        N = len(bloomDay)

        if m*k > N:
            return -1
    
        def possible(days):
            count = 0
            numBoq = 0
            for bloom in bloomDay:
                if bloom <= days:
                    count += 1
                    if count == k:
                        numBoq += 1
                        count = 0
                else:
                    count = 0
            return numBoq

        lo = min(bloomDay)
        hi = max(bloomDay)

        while lo < hi:
            mid = lo + (hi-lo) // 2
            if possible(mid) < m:
                lo = mid + 1
            else:
                hi = mid

        return lo