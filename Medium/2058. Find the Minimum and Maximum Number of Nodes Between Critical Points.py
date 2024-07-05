# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next
        nxt = head.next.next
        crit = []
        i = 2
        while nxt:
            if (prev.val < curr.val and nxt.val < curr.val) or (
                prev.val > curr.val and nxt.val > curr.val
            ):
                crit.append(i)
            prev = curr
            curr = nxt
            nxt = nxt.next
            i += 1

        n = len(crit)
        if n >= 2:
            maxDiff = crit[-1] - crit[0]
            minDiff = float("inf")
            for i in range(n - 1):
                diff = crit[i + 1] - crit[i]
                if diff < minDiff:
                    minDiff = diff
            return [minDiff, maxDiff]
        return [-1, -1]
