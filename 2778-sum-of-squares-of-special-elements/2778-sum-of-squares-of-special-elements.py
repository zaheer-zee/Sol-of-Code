class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums) 
        # return n
        summ = 0
        for i in range(len(nums)):
            if n % (i+1) == 0:
                summ += (nums[i]*nums[i])
        return summ

        
        # for i in nums:
        #     if n % i == 0:
        #         summ += i**2

        # return summ

        