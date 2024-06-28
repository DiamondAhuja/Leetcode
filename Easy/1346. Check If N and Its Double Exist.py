class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for num in arr:
            if num == 0:
                arr.remove(0)
                if num in arr:
                    return True
            if 2*num in arr:
                return True
        return False