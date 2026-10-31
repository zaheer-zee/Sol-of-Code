class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        dic = {}
        check = []
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        for i in dic:
            if dic[i] == 1:
                check.append(i)

        summ = 0
        for i in check:
            summ += i
        return summ

        
        