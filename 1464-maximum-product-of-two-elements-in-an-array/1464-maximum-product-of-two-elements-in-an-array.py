class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = []
        for i in range(len(nums) - 1):
            for j in range(i+1,len(nums)):
                pr = (nums[i] - 1)*(nums[j] - 1)
                res.append(pr)

        return max(res)

                
        