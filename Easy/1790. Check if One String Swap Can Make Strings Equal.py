class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        if s1 == s2:
            return True

        numDifferences = 0
        iDifferences = []

        for i in range(len(s1)):

            if s1[i] != s2[i]:

                numDifferences += 1
                iDifferences.append(i)

        if numDifferences != 2:
            return False

        return (
            s1[iDifferences[0]] == s2[iDifferences[1]]
            and s1[iDifferences[1]] == s2[iDifferences[0]]
        )
