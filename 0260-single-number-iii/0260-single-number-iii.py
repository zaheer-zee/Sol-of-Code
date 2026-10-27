class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        res = []
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1

            else:
                dic[i] = 1

        for i in dic:
            if dic[i] == 1:
                res.append(i)
        return res

        