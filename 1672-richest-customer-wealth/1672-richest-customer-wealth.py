class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        lis = []
        for i in accounts:
            summ = 0
            for j in i:
                summ += j

            lis.append(summ)
        return max(lis)
        