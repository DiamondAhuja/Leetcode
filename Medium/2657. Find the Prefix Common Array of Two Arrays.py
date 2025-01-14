class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        freq = []
        count = 0
        for i in range(len(A)):
            if A[i] not in freq:
                freq.append(A[i])
            else:
                count += 1
            if B[i] not in freq:
                freq.append(B[i])
            else:
                count += 1
            res.append(count)
        return res
