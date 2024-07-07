class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        filled = numBottles
        empty = numBottles
        drink = 0
        while filled:
            drink += filled
            filled = empty // numExchange
            empty = filled + (empty % numExchange)
        return drink
