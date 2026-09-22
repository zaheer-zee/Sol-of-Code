class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        count = 0

        for i in range(len(nums) - 1):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if abs(nums[j] - nums[i]) == diff and abs(nums[j] - nums[k]) == diff:
                        count += 1
        return count
        