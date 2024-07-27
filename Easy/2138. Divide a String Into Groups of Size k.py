from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        rem = n % k
        partitions = n // k
        index = 0
        output = []

        for i in range(partitions):
            output.append(s[index: index + k])
            index += k

        if rem != 0:
            x = s[-rem:] + fill*(k-rem)
            output.append(x)

        return output
