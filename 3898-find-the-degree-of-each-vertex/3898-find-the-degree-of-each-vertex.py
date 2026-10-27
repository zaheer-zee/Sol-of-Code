class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        res = []
        for i in matrix:
            summ = 0
            for j in i:
                summ += j
            res.append(summ)

        return res






        