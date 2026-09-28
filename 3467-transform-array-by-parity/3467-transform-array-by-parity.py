class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        for i in range(n):
            if nums[i]%2 == 1:
                ans[i] = 1

        ans.sort()
        return ans
        