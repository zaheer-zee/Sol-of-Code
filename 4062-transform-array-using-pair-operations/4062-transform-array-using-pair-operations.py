class Solution:
    def canTransform(self, source: list[int], target: list[int]) -> bool:
        summ1 = 0
        summ2 = 0
        for i in source:
            summ1 += i
        for j in target:
            summ2 += j

        if summ1 == summ2:
            return True
        else:
            return False
        