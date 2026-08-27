class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        oddSum = 0
        eveSum = 0
        i = 0
        while i < len(nums):
            if i % 2 == 0:
                eveSum += nums[i]
            elif i % 2 == 1:
                oddSum += nums[i]
            i += 1
        summ = eveSum - oddSum
        return summ        