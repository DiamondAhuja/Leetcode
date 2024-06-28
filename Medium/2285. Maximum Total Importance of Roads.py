class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        count = [0] * n
        for x, y in roads:
            count[x] += 1
            count[y] += 1
        count.sort(reverse=True)
        total = 0
        for x in count:
            total += x * n
            n -= 1
        return total