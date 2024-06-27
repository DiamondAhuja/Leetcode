class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        common = 0
        if edges[0][0] in edges[1]:
            common = edges[0][0]
        else:
            common = edges[0][1]
        return common