class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        i, direction = 1, 1
        while time:
            i += direction
            if i == 1 or i == n:
                direction *= -1
            time -= 1
        return i
