class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        numInd = 0
        expected = sorted(heights)
        for i in range (len(heights)):
            if heights[i] != expected[i]: 
                numInd += 1
        return numInd