class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        bmax = Counter()
        for b in words2:
            bmax |= Counter(b)
        result = []
        for a in words1:
            if all(a.count(char) >= bmax[char] for char in bmax):
                result.append(a)
        return result