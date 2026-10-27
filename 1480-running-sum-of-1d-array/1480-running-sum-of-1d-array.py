class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        res = []
        count = 0
        for i in nums:
            count += i
            res.append(count)

        return res
        