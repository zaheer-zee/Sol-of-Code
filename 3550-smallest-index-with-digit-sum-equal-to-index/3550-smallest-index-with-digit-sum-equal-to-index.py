class Solution:
    def smallestIndex(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            val = nums[i]
            summ = 0
            while val > 0:
                digit = val % 10
                summ += digit
                val //= 10

            if summ == i:
                return i
        return -1






        